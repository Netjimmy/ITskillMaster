# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('jobno', models.AutoField(serialize=False, primary_key=True)),
                ('src', models.CharField(max_length=50, null=True, blank=True)),
                ('postdate', models.DateField(null=True, blank=True)),
                ('title', models.CharField(max_length=150, null=True, blank=True)),
                ('company', models.CharField(max_length=150, null=True, blank=True)),
                ('industry', models.CharField(max_length=100, null=True, blank=True)),
                ('loc', models.CharField(max_length=50, null=True, blank=True)),
                ('emptype', models.CharField(max_length=50, null=True, blank=True)),
                ('exp', models.DecimalField(null=True, max_digits=3, decimal_places=1, blank=True)),
                ('salary', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('skill', models.TextField(null=True, blank=True)),
                ('url', models.CharField(unique=True, max_length=120)),
                ('cluster', models.SmallIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'job',
                'managed': False,
            },
        ),
    ]
