# Generated by Django 3.1.7 on 2021-04-05 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210404_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='slots',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
