# Generated by Django 2.1.3 on 2018-11-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_auto_20181122_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electricitymeters',
            name='value',
        ),
        migrations.RemoveField(
            model_name='electricitymeters',
            name='zone',
        ),
        migrations.RemoveField(
            model_name='watermeters',
            name='value',
        ),
        migrations.AddField(
            model_name='electricitymeters',
            name='valueDay',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='electricitymeters',
            name='valueNight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='watermeters',
            name='valueCold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='watermeters',
            name='valueHot',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='electricitymeters',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='watermeters',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
