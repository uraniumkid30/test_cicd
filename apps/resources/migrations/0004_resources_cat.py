# Generated by Django 5.1.6 on 2025-03-04 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.category'),
        ),
    ]
