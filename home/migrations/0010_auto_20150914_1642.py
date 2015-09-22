# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150914_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='SKU',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='item_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
