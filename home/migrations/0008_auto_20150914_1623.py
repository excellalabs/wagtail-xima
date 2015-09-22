# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150914_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryitem',
            old_name='image',
            new_name='pic',
        ),
    ]
