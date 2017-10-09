# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 00:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compromisso',
            name='convidado',
            field=models.ManyToManyField(related_name='Convidados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='institucional',
            field=models.BooleanField(verbose_name='Institucional'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='visivel',
            field=models.BooleanField(verbose_name='Visivel'),
        ),
    ]
