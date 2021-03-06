# Generated by Django 2.1.3 on 2018-11-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0009_auto_20181122_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('prediction', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='electricitymeters',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='watermeters',
            name='date',
            field=models.DateField(),
        ),
    ]
