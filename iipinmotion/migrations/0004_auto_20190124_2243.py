# Generated by Django 2.0.6 on 2019-01-24 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iipinmotion', '0003_auto_20190124_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='predicted_Stps',
            new_name='predicted_stps',
        ),
    ]
