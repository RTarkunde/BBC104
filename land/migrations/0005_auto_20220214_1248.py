# Generated by Django 3.2.12 on 2022-02-14 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='lead',
            name='email_id',
            field=models.EmailField(max_length=100),
        ),
    ]