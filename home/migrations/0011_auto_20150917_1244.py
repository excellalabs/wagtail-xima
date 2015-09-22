# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('home', '0010_auto_20150914_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='pic',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Please include a description of the product'),
        ),
    ]
