# Generated by Django 3.2.12 on 2022-02-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20220215_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='preferred_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='salarycontact',
            name='contact_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='salarycontact',
            name='current_organization',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='salarycontact',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
