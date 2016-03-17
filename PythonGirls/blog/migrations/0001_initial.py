# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-01 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('conteudo', models.CharField(max_length=60)),
                ('data_criacao', models.DateField()),
                ('data_modificacao', models.DateField()),
            ],
        ),
    ]