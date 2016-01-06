# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 11:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20160105_1929'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_auto_20160102_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_anonymous', models.BooleanField()),
                ('visibility', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('flags', models.ManyToManyField(blank=True, related_name='flagged_pictures', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture', to='location.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
