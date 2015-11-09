# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20151109_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historico',
            name='servicos',
        ),
        migrations.AddField(
            model_name='historico',
            name='servicos',
            field=models.ManyToManyField(to='manager.Servico'),
        ),
    ]
