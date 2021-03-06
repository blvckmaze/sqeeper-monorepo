# Generated by Django 4.0.4 on 2022-06-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0004_alter_note_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="content",
        ),
        migrations.AddField(
            model_name="note",
            name="description",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="note",
            name="title",
            field=models.CharField(max_length=64),
        ),
    ]
