# Generated by Django 3.2.17 on 2023-02-27 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_add_queue_display_priority_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketqueue',
            name='escalation_queue',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='escalates_to',
                related_query_name='escalates_to',
                to='tickets.ticketqueue',
            ),
        ),
    ]
