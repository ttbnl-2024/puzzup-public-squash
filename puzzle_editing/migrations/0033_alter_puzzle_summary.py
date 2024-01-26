# Generated by Django 4.2.2 on 2023-07-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("puzzle_editing", "0032_alter_puzzle_discord_emoji"),
    ]

    operations = [
        migrations.AlterField(
            model_name="puzzle",
            name="summary",
            field=models.TextField(
                blank=True,
                help_text=(
                    "A **non-spoilery description.** What will solvers see when they"
                    " open the puzzle?"
                ),
            ),
        ),
    ]
