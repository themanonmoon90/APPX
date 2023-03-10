# Generated by Django 4.1.3 on 2023-03-03 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0016_alter_shift_end_time_alter_shift_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2023, 3, 3, 20, 56, 55, 215182)),
        ),
        migrations.AlterField(
            model_name='shift',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2023, 3, 3, 20, 56, 55, 215182)),
        ),
        migrations.AlterField(
            model_name='student',
            name='preferred_start_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 3, 3, 20, 56, 55, 215182)),
        ),
    ]
