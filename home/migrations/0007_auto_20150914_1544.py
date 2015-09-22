# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150914_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='feed_image',
            new_name='image',
        ),
    ]
