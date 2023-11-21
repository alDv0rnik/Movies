# Generated by Django 4.2.6 on 2023-11-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(related_name='movie_director', to='catalog.director'),
        ),
    ]
