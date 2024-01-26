# Generated by Django 4.1.5 on 2023-02-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("puzzle_editing", "0011_testsolvesession_is_open"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testsolveparticipation",
            name="general_feedback",
            field=models.TextField(
                blank=True,
                help_text=(
                    "**General feedback**. What did you like & dislike about this"
                    " puzzle? Is there anything you think should be changed (e.g."
                    " amount of flavor/cluing, errata, tech issues, mechanics, theming,"
                    " etc.)?"
                ),
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="testsolveparticipation",
            name="misc_feedback",
            field=models.TextField(
                blank=True,
                help_text=(
                    "**Misc. feedback**. Anything else you want to add? If you were"
                    " spoiled, mention it here. (This can include: things you tried,"
                    " any shortcuts you found, break-ins, stuck points, accessibility)"
                ),
                null=True,
            ),
        ),
    ]
