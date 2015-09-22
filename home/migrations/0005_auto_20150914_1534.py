# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_inventoryitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='price',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
