from __future__ import annotations

import itertools
from collections.abc import Iterable

import requests
from django.conf import settings
from django.db.models import Q

import puzzle_editing.models as m
from puzzle_editing.discord import (
    Client,
    DiscordError,
    TextChannel,
    Thread,
    TimedCache,
    VoiceChannel,
)

# Global channel cache with a 10m timeout
_global_text_cache: TimedCache[str, TextChannel] = TimedCache(timeout=600)
_global_voice_cache: TimedCache[str, VoiceChannel] = TimedCache(timeout=600)
# Global thread cache with a 10m timeout
_global_thread_cache: TimedCache[str, Thread] = TimedCache(timeout=600)


def enabled():
    """Returns true if the django settings enable discord."""
    return (
        settings.DISCORD_BOT_TOKEN is not None and settings.DISCORD_GUILD_ID is not None
    )


def get_client() -> Client:
    """Gets a discord client, or raises and error if discord isn't enabled."""
    if not enabled():
        msg = (
            "Discord is not enabled. Make sure settings.DISCORD_BOT_TOKEN "
            "and settings.DISCORD_GUILD_ID are set."
        )
        raise DiscordError(msg)
    return Client(
        settings.DISCORD_BOT_TOKEN,
        settings.DISCORD_GUILD_ID,
        _global_text_cache,
        _global_voice_cache,
        _global_thread_cache,
    )


def init_perms(c: Client, u: m.User):
    """Update u's visibility on every puzzle they're an author/editor on.

    This can be slow, so we only call it if a user's discord_user_id changes.
    """
    if not c or not u.discord_user_id:
        return
    isAuthEd = Q(authors__pk=u.pk) | Q(editors__pk=u.pk)
    puzzles = set(m.Puzzle.objects.filter(isAuthEd))
    for p in puzzles:
        ch = get_channel(c, p)
        if ch is None:
            continue
        sync_puzzle_channel(p, ch)
        c.save_channel(ch)


def get_dids(users: Iterable[m.User]) -> Iterable[str]:
    """Get the discord uids of all provided users that have them."""
    for user in users:
        if user.discord_user_id:
            yield user.discord_user_id


def tag_id(discord_id: str) -> str:
    """Formats a discord id as a tag for a message."""
    return f"<@{discord_id}>"


def channel_tag(discord_id: str) -> str:
    return f"<#{discord_id}>"


def get_tags(users: Iterable[m.User], skip_missing: bool = True) -> list[str]:
    """Get discord @tags from a bunch of users.

    Users without discord ids will be skipped, unless skip_missing is False, in
    which case their names will be returned instead of discord tags.
    """
    items = []
    for user in users:
        if user.discord_user_id:
            items.append(user.discord_tag)
        elif not skip_missing:
            items.append(user.credits_name)
    return items


def get_channel(c: Client, p: m.Puzzle) -> TextChannel | None:
    """Get the channel for a puzzle, or None if hasn't got one.

    If the puzzle has a discord_channel_id set, but no channel has that id,
    this will also return None (this indicates that someone deleted the channel
    from the discord side)
    """
    if not p.discord_channel_id:
        return None
    try:
        # If our id is valid, return the fetched channel.
        return c.get_text_channel(p.discord_channel_id)
    except requests.HTTPError as e:
        if e.response.status_code != 404:
            # Not 400 -> something else went wrong. Abort.
            raise
        # 400 -> we have a bad channel id (maybe someone deleted
        # the channel). Clear it.
        return None


def get_thread(c: Client, s: m.TestsolveSession) -> Thread | None:
    """Get the thread for a testsolving session, or None if hasn't got one.
    If the session has a discord_thread_id set, but no thread has that id,
    this will also return None (this indicates that someone deleted the thread
    from the discord side)
    """
    if not s.discord_thread_id:
        return None
    try:
        return c.get_thread(s.discord_thread_id)
    except requests.HTTPError as e:
        if e.response.status_code != 404:
            raise
        return None


def get_client_and_channel(p: m.Puzzle) -> tuple[Client | None, TextChannel | None]:
    """Shorthand for get_client followed by get_channel.

    Returns (client, channel); both will be None if discord is disabled, and
    channel will be None if the puzzle doesn't have one.
    """
    if not enabled():
        return None, None
    c = get_client()
    ch = get_channel(c, p)
    return c, ch


def sync_puzzle_channel(
    puzzle: m.Puzzle, tc: TextChannel, url: str | None = None, sync_users: bool = True
) -> TextChannel:
    """Syncs data from a puzzle to its TextChannel.

    This will update the channel name, topic, and permissions.

    If sync_users is true, this will query for all authors, editors, and
    spoiled users on this puzzle, and will ensure that A) every author and
    editor is in the channel, and B) anyone who isn't spoiled is removed from
    the channel.
    """
    tc.name = f"{puzzle.id:03d}-{puzzle.name:.96}"
    if url:
        tc.topic = url
    if not sync_users:
        return tc
    # Update individual user permissions
    # every author/editor MUST see the channel
    autheds = itertools.chain(puzzle.authors.all(), puzzle.editors.all())
    # this discord bot MUST see the channel
    must_see = set(get_dids(autheds)) | {settings.DISCORD_CLIENT_ID}
    # anyone who is spoiled CAN see the channel
    can_see = set(get_dids(puzzle.spoiled.all()))
    # Loop over all users who must see and all who currently have overwrites;
    # add VIEW_CHANNEL to those who must have it and remove VIEW_CHANNEL from
    # those who can't have it. If someone is a spoiled user but not an author
    # or an editor, their status will be unchanged.
    current = set(tc.perms.user_ids())
    for uid in must_see | current:
        if uid in must_see:
            tc.perms.update_user(uid, allow="VIEW_CHANNEL")
        elif uid not in can_see:
            tc.perms.update_user(uid, ignore="VIEW_CHANNEL")
    return tc


def build_testsolve_admin_thread(puzzle: m.Puzzle, guild_id: str):
    puzzle_type = "Meta" if puzzle.is_meta else "Feeder"
    return Thread(
        id="",
        type=11,
        name=f"{puzzle_type} {puzzle.id}",
        guild_id=guild_id,
        parent_id=settings.DISCORD_TESTSOLVE_ADMIN_CHANNEL_ID,
    )


def build_testsolve_thread(session: m.TestsolveSession, guild_id: str):
    return Thread(
        id="",
        type=12,
        name=f"{session.puzzle.puzzle_type} {session.puzzle.id} - Session {session.id}",
        guild_id=guild_id,
        parent_id=settings.DISCORD_TESTSOLVE_CHANNEL_ID,
    )


def build_puzzle_channel(
    url: str, puzzle: m.Puzzle, guild_id: str, private: bool = True
) -> TextChannel:
    """Builds a new TextChannel for a puzzle.

    url should be the absolute url to the puzzle, i.e. it should start with
    "http", because it's going to go into the discord topic.

    The channel will have an appropriate name and topic, and will have
    allow=VIEW_CHANNEL overwrites for all authors and editors. If private is
    True (the default), it will deny VIEW_CHANNEL to @everyone.

    This does NOT save the channel to discord - the caller must do that
    themselves. It also ONLY adds the authors and editors - if there are other
    users you want to have permission, you should add them yourself.
    """
    tc = TextChannel(id="", name=puzzle.name, guild_id=guild_id)
    sync_puzzle_channel(puzzle, tc, url=url)
    if private:
        tc.make_private()
    return tc


def announce_ppl(
    c: Client,
    ch: TextChannel,
    spoiled: Iterable[m.User] = (),
    editors: Iterable[m.User] = (),
):
    """Announces new spoiled users and editors.

    If c or ch is None we do nothing.
    """
    if c is None or ch is None:
        return
    msg = []
    editors = set(editors)
    spoiled = set(spoiled) - set(editors)
    if spoiled:
        tags = get_tags(spoiled, skip_missing=False)
        msg.append(f"Newly spoiled: {', '.join(tags)}")
    # Announce newly assigned editors
    if editors:
        tags = get_tags(editors, skip_missing=False)
        msg.append(f"New editor(s): {', '.join(tags)}")
    if msg:
        c.post_message(ch.id, "\n".join(msg))
