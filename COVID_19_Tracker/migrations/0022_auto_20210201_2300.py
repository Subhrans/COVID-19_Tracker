# Generated by Django 3.0.1 on 2021-02-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COVID_19_Tracker', '0021_auto_20210201_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='india',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='india',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True),
        ),
    ]