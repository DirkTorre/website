# Generated by Django 4.1 on 2024-07-06 12:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_reviews', '0002_rename_id_movie_ttnumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netflix', models.BooleanField(null=True)),
                ('prime', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WatchedDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_date', models.DateField()),
                ('enjoyment', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
            ],
        ),
        migrations.CreateModel(
            name='WatchedStatus',
            fields=[
                ('ttconst', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='scores',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Scores',
        ),
        migrations.AddField(
            model_name='watcheddates',
            name='ttconst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie_reviews.watchedstatus'),
        ),
        migrations.AddField(
            model_name='availability',
            name='ttconst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie_reviews.watchedstatus'),
        ),
    ]
