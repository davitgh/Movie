# Generated by Django 2.0.13 on 2019-08-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='slider_movies',
            field=models.IntegerField(),
        ),
    ]
