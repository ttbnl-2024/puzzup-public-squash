# Generated by Django 4.2.2 on 2023-06-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("puzzle_editing", "0029_alter_hint_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="puzzle",
            name="status",
            field=models.CharField(
                choices=[
                    ("II", "Initial Idea"),
                    ("AE", "Awaiting Approval By EIC"),
                    ("ND", "EICs are Discussing"),
                    ("ID", "Idea in Development"),
                    ("AA", "Awaiting Answer"),
                    ("W", "Writing (Answer Assigned)"),
                    ("AT", "Awaiting Approval for Testsolving"),
                    ("PF", "Needs Pre-Testsolve Factcheck"),
                    ("FR", "Factcheck Revisions"),
                    ("T", "Ready to be Testsolved"),
                    ("TT", "Actively Testsolving"),
                    ("TR", "Awaiting Testsolve Review"),
                    ("R", "Revising (Needs Testsolving)"),
                    ("AO", "Awaiting Approval (Done with Testsolving)"),
                    ("NH", "Needs Hints"),
                    ("AH", "Awaiting Hints Approval"),
                    ("PB", "Postproduction Blocked"),
                    ("BT", "Postproduction Blocked On Tech Request"),
                    ("NP", "Ready for Postprodding"),
                    ("PP", "Actively Postprodding"),
                    ("AP", "Awaiting Approval After Postprod"),
                    ("NF", "Needs Postprod Factcheck"),
                    ("NC", "Needs Copy Edits"),
                    ("NR", "Needs Final Revisions"),
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
                    ("ID", "Idea in Development"),
                    ("AA", "Awaiting Answer"),
                    ("W", "Writing (Answer Assigned)"),
                    ("AT", "Awaiting Approval for Testsolving"),
                    ("PF", "Needs Pre-Testsolve Factcheck"),
                    ("FR", "Factcheck Revisions"),
                    ("T", "Ready to be Testsolved"),
                    ("TT", "Actively Testsolving"),
                    ("TR", "Awaiting Testsolve Review"),
                    ("R", "Revising (Needs Testsolving)"),
                    ("AO", "Awaiting Approval (Done with Testsolving)"),
                    ("NH", "Needs Hints"),
                    ("AH", "Awaiting Hints Approval"),
                    ("PB", "Postproduction Blocked"),
                    ("BT", "Postproduction Blocked On Tech Request"),
                    ("NP", "Ready for Postprodding"),
                    ("PP", "Actively Postprodding"),
                    ("AP", "Awaiting Approval After Postprod"),
                    ("NF", "Needs Postprod Factcheck"),
                    ("NC", "Needs Copy Edits"),
                    ("NR", "Needs Final Revisions"),
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
                    ("ID", "Idea in Development"),
                    ("AA", "Awaiting Answer"),
                    ("W", "Writing (Answer Assigned)"),
                    ("AT", "Awaiting Approval for Testsolving"),
                    ("PF", "Needs Pre-Testsolve Factcheck"),
                    ("FR", "Factcheck Revisions"),
                    ("T", "Ready to be Testsolved"),
                    ("TT", "Actively Testsolving"),
                    ("TR", "Awaiting Testsolve Review"),
                    ("R", "Revising (Needs Testsolving)"),
                    ("AO", "Awaiting Approval (Done with Testsolving)"),
                    ("NH", "Needs Hints"),
                    ("AH", "Awaiting Hints Approval"),
                    ("PB", "Postproduction Blocked"),
                    ("BT", "Postproduction Blocked On Tech Request"),
                    ("NP", "Ready for Postprodding"),
                    ("PP", "Actively Postprodding"),
                    ("AP", "Awaiting Approval After Postprod"),
                    ("NF", "Needs Postprod Factcheck"),
                    ("NC", "Needs Copy Edits"),
                    ("NR", "Needs Final Revisions"),
                    ("D", "Done"),
                    ("DF", "Deferred"),
                    ("X", "Dead"),
                ],
                max_length=2,
            ),
        ),
    ]
