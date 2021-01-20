# Generated by Django 3.0.1 on 2021-01-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=10000, unique=True)),
                ('country', models.CharField(max_length=1000)),
                ('countryCode', models.CharField(max_length=100)),
                ('slugId', models.SlugField(unique=True)),
                ('newConfirmed', models.IntegerField()),
                ('totalConfirmed', models.IntegerField()),
                ('newDeaths', models.IntegerField()),
                ('totalDeaths', models.IntegerField()),
                ('newRecovered', models.IntegerField()),
                ('totalRecoverd', models.BigIntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Global',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.CharField(max_length=100000, unique=True)),
                ('newConfirmed', models.IntegerField()),
                ('totalConfirmed', models.IntegerField()),
                ('newDeaths', models.IntegerField()),
                ('totalDeaths', models.IntegerField()),
                ('newRecovered', models.IntegerField()),
                ('totalRecoverd', models.BigIntegerField()),
            ],
        ),
    ]
