# Generated by Django 4.1.2 on 2022-10-31 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0006_review_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings_count',
            field=models.IntegerField(default=0),
        ),
    ]
