# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150914_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='pic',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Please include a description of the product as necessary as well as an image'),
        ),
    ]
