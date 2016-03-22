# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('no', models.IntegerField(serialize=False, primary_key=True)),
                ('loc', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-postdate'], 'managed': False},
        ),
    ]
