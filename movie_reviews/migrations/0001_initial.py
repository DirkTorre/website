# Generated by Django 4.1 on 2024-05-07 21:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('watched', models.BooleanField(null=True)),
                ('priority', models.BooleanField(default=False)),
                ('netflix', models.BooleanField(null=True)),
                ('prime', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_date', models.DateField()),
                ('enjoyment', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('story', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('subject', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('acting', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('script', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('visual', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('action', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('comedy', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_reviews.movie')),
            ],
        ),
    ]