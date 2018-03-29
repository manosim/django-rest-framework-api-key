# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_api_key', '0002_path_re'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('path_re', models.CharField(max_length=1024)),
            ],
        ),
        migrations.RemoveField(
            model_name='apikey',
            name='path_re',
        ),
        migrations.AddField(
            model_name='apikey',
            name='owner',
            field=models.ForeignKey(to='rest_framework_api_key.KeyOwner', null=True),
        ),
    ]
