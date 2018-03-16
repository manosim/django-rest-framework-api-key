# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_api_key', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikey',
            name='path_re',
            field=models.CharField(default='*', max_length=1024),
            preserve_default=False,
        ),
    ]
