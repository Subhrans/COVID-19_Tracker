# Generated by Django 3.0.1 on 2021-01-21 23:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('COVID_19_Tracker', '0010_auto_20210121_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='global',
            name='update_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
