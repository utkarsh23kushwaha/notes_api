# Generated by Django 4.2.5 on 2024-01-05 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_note_newginindex_note_newginindex'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='note',
            name='NewGinIndex',
        ),
    ]
