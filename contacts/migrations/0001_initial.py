# Generated by Django 3.2.12 on 2022-02-14 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('email_id', models.EmailField(max_length=100)),
                ('contact_no', models.TextField(max_length=12)),
                ('prefered_time', models.TextField(max_length=100)),
                ('country', models.TextField(max_length=100)),
                ('zip_code', models.IntegerField()),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('email_id', models.EmailField(max_length=100)),
                ('contact_no', models.TextField(max_length=12)),
                ('current_organization', models.TextField(max_length=100)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('salary_income', models.IntegerField()),
                ('rental_income', models.IntegerField()),
                ('interest_income', models.IntegerField()),
                ('capital_gains', models.IntegerField()),
                ('other_income', models.IntegerField()),
                ('marked_for_delete', models.BooleanField(default=False)),
                ('send_to_salesforce', models.BooleanField(default=False)),
                ('sent_to_salesforce', models.BooleanField(default=False)),
                ('send_to_csv', models.BooleanField(default=False)),
                ('sent_to_csv', models.BooleanField(default=False)),
            ],
        ),
    ]