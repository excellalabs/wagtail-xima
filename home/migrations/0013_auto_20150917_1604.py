# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150917_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='SKU',
            field=models.TextField(null=True, blank=True),
        ),
    ]
