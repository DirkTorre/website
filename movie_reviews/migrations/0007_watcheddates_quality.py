# Generated by Django 4.1 on 2024-08-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0006_alter_availability_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watcheddates',
            name='quality',
            field=models.SmallIntegerField(null=True),
        ),
    ]
