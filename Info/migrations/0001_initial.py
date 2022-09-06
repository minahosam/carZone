# Generated by Django 4.1 on 2022-08-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('work_days', models.CharField(max_length=200)),
                ('work_hours', models.CharField(max_length=200)),
                ('facebook_link', models.CharField(max_length=200)),
                ('twitter_link', models.CharField(max_length=200)),
                ('google_link', models.CharField(max_length=200)),
                ('linkedin_link', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
