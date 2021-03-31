# Generated by Django 3.1.2 on 2021-02-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rootApp', '0003_auto_20201006_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FID_1', models.CharField(max_length=10)),
                ('BLDG_ID', models.CharField(max_length=10)),
                ('HEIGHT', models.CharField(max_length=10)),
                ('FOOTPRINT', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=200)),
                ('no_floors', models.CharField(max_length=10)),
                ('DATA_YEAR', models.CharField(max_length=10)),
                ('SFT', models.CharField(max_length=10)),
                ('Area_SqMet', models.CharField(max_length=30)),
                ('FloodDepth10Year', models.CharField(max_length=10)),
                ('FloodDepth50Year', models.CharField(max_length=10)),
                ('FloodDepth100Year', models.CharField(max_length=10)),
                ('FloodDepth500Year', models.CharField(max_length=10)),
                ('ElevationUSGS2017', models.CharField(max_length=30)),
                ('Elevation_Jefferson', models.CharField(max_length=30)),
                ('Elevatio_2019USGS', models.CharField(max_length=30)),
                ('parish', models.CharField(max_length=100)),
                ('floodzone', models.CharField(max_length=100)),
                ('Source', models.CharField(max_length=10)),
                ('u_intercept', models.CharField(max_length=30)),
                ('a_slope', models.CharField(max_length=30)),
            ],
        ),
    ]
