# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20151109_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historico',
            name='valor_total',
        ),
    ]
