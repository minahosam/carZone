# Generated by Django 4.1 on 2022-08-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Info', '0002_alter_info_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='mobile_number',
            field=models.CharField(max_length=20),
        ),
    ]
