# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20151023_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Awful'), (2, 'Not Bad'), (3, 'Good'), (4, 'Pretty Good'), (5, 'Amazing')]),
        ),
    ]
