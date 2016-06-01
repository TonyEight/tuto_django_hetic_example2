# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, unique=True)),
                ('color', models.CharField(choices=[(0, 'red'), (1, 'black')], max_length=1)),
            ],
        ),
    ]
