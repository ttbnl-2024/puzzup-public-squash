# Generated by Django 4.1.7 on 2023-02-27 04:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("puzzle_editing", "0013_puzzleanswer_case_sensitive_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="puzzle",
            name="quickcheckers",
            field=models.ManyToManyField(
                blank=True,
                related_name="quickchecking_puzzles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="puzzle",
            name="status",
            field=models.CharField(
                choices=[
                    ("II", "Initial Idea"),
                    ("AE", "Awaiting Approval By EIC"),
                    ("ND", "EICs are Discussing"),
                    ("AR", "Awaiting Input By Editor"),
                    ("ID", "Idea in Development"),
                    ("AA", "Awaiting Answer"),
                    ("W", "Writing (Answer Assigned)"),
                    ("AT", "Awaiting Approval for Testsolving"),
                    ("PF", "Needs Pre-Testsolve Factcheck"),
                    ("T", "Ready to be Testsolved"),
                    ("TR", "Awaiting Testsolve Review"),
                    ("R", "Revising (Needs Testsolving)"),
                    ("RP", "Revising (Done with Testsolving)"),
                    ("AO", "Awaiting Approval (Done with Testsolving)"),
                    ("PB", "Postproduction Blocked"),
                    ("BT", "Postproduction Blocked On Tech Request"),
                    ("NP", "Ready for Postprodding"),
                    ("PP", "Actively Postprodding"),
                    ("AP", "Awaiting Approval After Postprod"),
                    ("NF", "Needs Factcheck"),
                    ("NC", "Needs Copy Edits"),
                    ("NR", "Needs Final Revisions"),
                    ("NH", "Needs Hints"),
                    ("AH", "Awaiting Hints Approval"),
                    ("D", "Done"),
                    ("DF", "Deferred"),
                    ("X", "Dead"),
                ],
                default="II",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="puzzlecomment",
            name="status_change",
            field=models.CharField(
                blank=True,
                choices=[
                    ("II", "Initial Idea"),
                    ("AE", "Awaiting Approval By EIC"),
                    ("ND", "EICs are Discussing"),
                    ("AR", "Awaiting Input By Editor"),
                    ("ID", "Idea in Development"),
                    ("AA", "Awaiting Answer"),
                    ("W", "Writing (Answer Assigned)"),
                    ("AT", "Awaiting Approval for Testsolving"),
                    ("PF", "Needs Pre-Testsolve Factcheck"),
                    ("T", "Ready to be Testsolved"),
                    ("TR", "Awaiting Testsolve Review"),
                    ("R", "Revising (Needs Testsolving)"),
                    ("RP", "Revising (Done with Testsolving)"),
                    ("AO", "Awaiting Approval (Done with Testsolving)"),
                    ("PB", "Postproduction Blocked"),
                    ("BT", "Postproduction Blocked On Tech Request"),
                    ("NP", "Ready for Postprodding"),
                    ("PP", "Actively Postprodding"),
                    ("AP", "Awaiting Approval After Postprod"),
                    ("NF", "Needs Factcheck"),
                    ("NC", "Needs Copy Edits"),
                    ("NR", "Needs Final Revisions"),
                    ("NH", "Needs Hints"),
                    ("AH", "Awaiting Hints Approval"),
                    ("D", "Done"),
                    ("DF", "Deferred"),
                    ("X", "Dead"),
                ],
                help_text=(
                    "Any status change caused by this comment. Only used for recording"
                    " history and computing statistics; not a source of truth (i.e. the"
                    " puzzle will still store its current status, and this field's"
                    " value on any comment doesn't directly imply anything about that"
                    " in any technically enforced way)."
                ),
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="statussubscription",
            name="status",
            field=models.CharField(
                choices=[
                    ("II", "Initial Idea"),
                    ("AE", "Awaiting Approval By EIC"),
                    ("ND", "EICs are Discussing"),
                    ("AR", "Awaiting Input By Editor"),
                    ("ID", "Idea in Development"),
                    ("AA", "Awaiting Answer"),
                    ("W", "Writing (Answer Assigned)"),
                    ("AT", "Awaiting Approval for Testsolving"),
                    ("PF", "Needs Pre-Testsolve Factcheck"),
                    ("T", "Ready to be Testsolved"),
                    ("TR", "Awaiting Testsolve Review"),
                    ("R", "Revising (Needs Testsolving)"),
                    ("RP", "Revising (Done with Testsolving)"),
                    ("AO", "Awaiting Approval (Done with Testsolving)"),
                    ("PB", "Postproduction Blocked"),
                    ("BT", "Postproduction Blocked On Tech Request"),
                    ("NP", "Ready for Postprodding"),
                    ("PP", "Actively Postprodding"),
                    ("AP", "Awaiting Approval After Postprod"),
                    ("NF", "Needs Factcheck"),
                    ("NC", "Needs Copy Edits"),
                    ("NR", "Needs Final Revisions"),
                    ("NH", "Needs Hints"),
                    ("AH", "Awaiting Hints Approval"),
                    ("D", "Done"),
                    ("DF", "Deferred"),
                    ("X", "Dead"),
                ],
                max_length=2,
            ),
        ),
    ]
