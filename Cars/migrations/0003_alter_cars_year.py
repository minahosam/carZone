# Generated by Django 4.1 on 2022-08-12 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0002_alter_cars_description_alter_cars_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='year',
            field=models.CharField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], max_length=4),
        ),
    ]
