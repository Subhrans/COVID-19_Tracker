# Generated by Django 3.0.1 on 2021-01-20 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('COVID_19_Tracker', '0007_india'),
    ]

    operations = [
        migrations.RenameField(
            model_name='india',
            old_name='statecode',
            new_name='state_code',
        ),
    ]
