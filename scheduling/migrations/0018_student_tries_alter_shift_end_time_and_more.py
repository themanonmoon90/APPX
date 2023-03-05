# Generated by Django 4.1.3 on 2023-03-05 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0017_alter_shift_end_time_alter_shift_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='tries',
            field=models.PositiveBigIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='shift',
            name='end_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 3, 5, 19, 27, 44, 501610)),
        ),
        migrations.AlterField(
            model_name='shift',
            name='start_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 3, 5, 19, 27, 44, 501610)),
        ),
        migrations.AlterField(
            model_name='student',
            name='preferred_start_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 3, 5, 19, 27, 44, 501610)),
        ),
    ]
