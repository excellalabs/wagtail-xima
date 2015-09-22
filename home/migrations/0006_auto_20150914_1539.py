# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0005_auto_20150914_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='description',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='feed_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
    ]
