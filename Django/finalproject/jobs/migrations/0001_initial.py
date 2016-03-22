# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobstored',
            fields=[
                ('jobno', models.AutoField(serialize=False, primary_key=True)),
                ('srcno', models.CharField(max_length=30, null=True, blank=True)),
                ('postdate', models.DateField(null=True, blank=True)),
                ('title', models.CharField(max_length=150, null=True, blank=True)),
                ('company', models.CharField(max_length=150, null=True, blank=True)),
                ('industry', models.CharField(max_length=50, null=True, blank=True)),
                ('locno', models.CharField(max_length=150, null=True, blank=True)),
                ('emptypeno', models.CharField(max_length=50, null=True, blank=True)),
                ('exp', models.CharField(max_length=100, null=True, blank=True)),
                ('salary', models.CharField(max_length=100, null=True, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('url', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'db_table': 'jobstored',
                'managed': False,
            },
        ),
    ]
