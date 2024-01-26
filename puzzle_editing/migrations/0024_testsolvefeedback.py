# Generated by Django 4.2.1 on 2023-05-27 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("puzzle_editing", "0023_puzzleanswer_special_sensitive"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestsolveFeedback",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "solve_path",
                    models.TextField(
                        blank=True,
                        help_text=(
                            "**Solve path**. What was the path you used to solve?"
                        ),
                    ),
                ),
                (
                    "general_feedback",
                    models.TextField(
                        blank=True,
                        help_text=(
                            "**General feedback**. What did you like & dislike about"
                            " this puzzle? Is there anything you think should be"
                            " changed (e.g. amount of flavor/cluing, errata, tech"
                            " issues, mechanics, theming, etc.)?"
                        ),
                    ),
                ),
                (
                    "aspects_accessibility",
                    models.TextField(
                        blank=True,
                        help_text=(
                            "Any accessibility concerns you'd like to raise? (alt text,"
                            " color, transcripts, subtitles, tooltips, keyboard"
                            " navigation, printing, etc.)"
                        ),
                    ),
                ),
                (
                    "comment",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="testsolve_feedback",
                        to="puzzle_editing.puzzlecomment",
                    ),
                ),
                (
                    "participation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedbacks",
                        to="puzzle_editing.testsolveparticipation",
                    ),
                ),
            ],
        ),
    ]
