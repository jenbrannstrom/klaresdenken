# Generated by Django 2.2.2 on 2019-06-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_auto_20190625_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='problem',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
