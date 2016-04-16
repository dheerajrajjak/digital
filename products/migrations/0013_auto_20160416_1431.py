# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='height',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='thumbnail',
            name='width',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
