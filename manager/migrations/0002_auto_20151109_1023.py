# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='historico',
        ),
        migrations.AddField(
            model_name='historico',
            name='servicos',
            field=models.ForeignKey(to='manager.Servico', default=1),
            preserve_default=False,
        ),
    ]
