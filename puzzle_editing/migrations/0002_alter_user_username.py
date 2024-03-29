# Generated by Django 4.1.5 on 2023-02-05 02:39

from django.db import migrations, models
import puzzle_editing.models


class Migration(migrations.Migration):
    dependencies = [
        ("puzzle_editing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text=(
                    "Required. 150 characters or fewer. Letters, digits and @/./#/+/-/_"
                    " only."
                ),
                max_length=150,
                unique=True,
                validators=[puzzle_editing.models.CustomUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
