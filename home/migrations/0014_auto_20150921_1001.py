# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20150917_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='stocked_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='SKU',
            field=models.TextField(max_length=8, null=True, blank=True),
        ),
    ]
