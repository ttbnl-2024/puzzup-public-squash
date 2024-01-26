# Generated by Django 4.1.7 on 2023-03-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("puzzle_editing", "0014_puzzle_quickcheckers_alter_puzzle_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="testsolveparticipation",
            name="solve_path",
            field=models.TextField(
                blank=True, help_text="What was the path you used to solve?", null=True
            ),
        ),
        migrations.AlterField(
            model_name="testsolveparticipation",
            name="aspects_accessibility",
            field=models.TextField(
                blank=True,
                help_text=(
                    "Any accessibility concerns you'd like to raise? (alt text, color,"
                    " transcripts, subtitles, tooltips, keyboard navigation, printing,"
                    " etc.)"
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
                    " any shortcuts you found, break-ins, stuck points)"
                ),
                null=True,
            ),
        ),
    ]
