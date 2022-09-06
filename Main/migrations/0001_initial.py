# Generated by Django 4.1 on 2022-08-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='team/')),
                ('facebook_link', models.URLField(max_length=500)),
                ('google_link', models.URLField(max_length=500)),
                ('twitter_link', models.URLField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]