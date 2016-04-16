# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'C:\\Users\\Dhiraj\\Dropbox\\digital\\static_cdn\\protected'), null=True, upload_to=products.models.media_upload_location, blank=True),
        ),
    ]
