# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('celular', models.CharField(max_length=20, verbose_name=b'N\xc3\xbamero de celular')),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre', blank=True)),
                ('apellido', models.CharField(max_length=50, verbose_name=b'Apellido', blank=True)),
                ('apellidoMaterno', models.CharField(max_length=50, verbose_name=b'Apellido materno', blank=True)),
                ('cedula', models.CharField(max_length=20, verbose_name=b'C\xc3\xa9dula', blank=True)),
                ('direccionfactura', models.CharField(max_length=150, verbose_name=b'Direcci\xc3\xb3n', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
