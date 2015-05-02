# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='marca',
            field=models.OneToOneField(to='solicitar.Marca'),
        ),
        migrations.AlterField(
            model_name='reparacion',
            name='modelo',
            field=models.OneToOneField(to='solicitar.Modelo'),
        ),
    ]
