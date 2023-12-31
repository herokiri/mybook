# Generated by Django 4.2.5 on 2023-10-05 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('description', models.CharField(default='Нету информации', max_length=2500, verbose_name='Об авторе')),
                ('img', models.ImageField(default='null', upload_to='books/authors_images/', verbose_name='Изображение автора')),
            ],
            options={
                'permissions': [('can_add_new_author', 'Can add new author'), ('can_delete_author', 'Can delete author')],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название категории')),
            ],
            options={
                'permissions': [('can_add_new_category', 'Can add new category'), ('can_delete_category', 'Can delete category')],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.CharField(max_length=2500, verbose_name='Описание')),
                ('img', models.ImageField(upload_to='books/books_images/', verbose_name='Картинка')),
                ('file', models.FileField(upload_to='books/file_books/% Y/% m/% d/', verbose_name='Файл')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.category')),
            ],
            options={
                'permissions': [('can_add_new_book', 'Can add new book'), ('can_delete_book', 'Can delete book')],
            },
        ),
    ]
