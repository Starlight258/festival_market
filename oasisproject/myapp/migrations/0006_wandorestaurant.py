# Generated by Django 3.2.14 on 2022-07-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_productdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='wandoRestaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('location', models.CharField(default='', max_length=50)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
        ),
    ]
