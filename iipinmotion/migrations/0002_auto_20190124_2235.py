# Generated by Django 2.0.6 on 2019-01-24 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iipinmotion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='percentage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='predictedStps',
            field=models.PositiveIntegerField(default=0),
        ),
    ]