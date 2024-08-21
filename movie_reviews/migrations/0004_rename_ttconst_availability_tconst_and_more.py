# Generated by Django 4.1 on 2024-07-07 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0003_availability_watcheddates_watchedstatus_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='ttconst',
            new_name='tconst',
        ),
        migrations.RenameField(
            model_name='watcheddates',
            old_name='ttconst',
            new_name='tconst',
        ),
        migrations.RenameField(
            model_name='watchedstatus',
            old_name='ttconst',
            new_name='tconst',
        ),
        migrations.AlterField(
            model_name='watcheddates',
            name='enjoyment',
            field=models.SmallIntegerField(),
        ),
    ]
