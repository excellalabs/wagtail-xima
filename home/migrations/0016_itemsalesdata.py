# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_inventoryitem_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSalesData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.IntegerField(default=1)),
                ('stocked', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('product', models.ForeignKey(to='home.InventoryItem')),
            ],
        ),
    ]
