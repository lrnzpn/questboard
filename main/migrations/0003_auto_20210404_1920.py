# Generated by Django 3.1.7 on 2021-04-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210404_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='is_for_everyone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quest',
            name='slots',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
