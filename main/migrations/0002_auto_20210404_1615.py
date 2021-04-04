# Generated by Django 3.1.7 on 2021-04-04 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='questboard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.questboard'),
        ),
        migrations.AddField(
            model_name='quest',
            name='slug',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='questboard',
            name='slug',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='stars',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questboard',
            name='required_stars',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='quest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.quest'),
        ),
    ]