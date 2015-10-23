# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from play import load_movie_title, load_rater_data, load_rating_data


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_movie_title),

        migrations.RunPython(load_rater_data),

        migrations.RunPython(load_rating_data)
    ]
