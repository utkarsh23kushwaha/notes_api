# Generated by Django 4.2.5 on 2024-01-06 21:10

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_note_newginindex'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='note',
            index=django.contrib.postgres.indexes.GinIndex(fields=['title', 'content'], name='NewGinIndex', opclasses=['gin_trgm_ops', 'gin_trgm_ops']),
        ),
    ]
