# Generated by Django 2.2.15 on 2020-09-15 18:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_chat', '0002_auto_20200915_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicchatroom',
            name='users',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, default=list, help_text='primary keys of users who are connected to chat room.', null=True, size=None, unique=True),
        ),
    ]
