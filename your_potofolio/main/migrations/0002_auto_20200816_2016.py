# Generated by Django 3.1 on 2020-08-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
