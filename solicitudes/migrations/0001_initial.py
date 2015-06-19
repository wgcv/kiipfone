# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('solicitar', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=1000)),
                ('leido', models.BooleanField(default=False)),
                ('coordinado', models.BooleanField(default=False)),
                ('finalizado', models.BooleanField(default=False)),
                ('color', models.ForeignKey(to='solicitar.Color', blank=True)),
                ('marca', models.ForeignKey(to='solicitar.Marca', blank=True)),
                ('modelo', models.ForeignKey(to='solicitar.Modelo', blank=True)),
                ('reparacion', models.ForeignKey(to='solicitar.Reparacion', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
