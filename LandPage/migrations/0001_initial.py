# Generated by Django 2.1.3 on 2018-11-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('partonymic', models.CharField(max_length=30)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('creationDate', models.DateTimeField()),
            ],
        ),
    ]
