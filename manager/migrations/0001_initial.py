# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('data_admissao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_demissao', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('data_chamado', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_realizacao', models.DateTimeField(blank=True, null=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacao', models.TextField()),
                ('cliente', models.ForeignKey(to='manager.Cliente')),
                ('funcionario', models.ForeignKey(to='manager.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('historico', models.ForeignKey(to='manager.Historico')),
            ],
        ),
    ]
