# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 09:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '0002_auto_20160515_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preview_images', to='session.Session')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='previewimage',
            unique_together=set([('session', 'order')]),
        ),
    ]
