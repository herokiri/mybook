# Generated by Django 4.2.5 on 2023-10-05 11:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Издательство')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='book',
            name='year_of_publishing',
            field=models.IntegerField(default=2023, verbose_name='Год издания'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='books.publishinghouse'),
        ),
    ]
