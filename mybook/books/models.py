from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class PublishingHouse(models.Model):
    name = models.CharField("Издательство", max_length=200, unique=True)


class Category(models.Model):
    name = models.CharField("Название категории", max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_add_new_category", "Can add new category"),
            ("can_delete_category", "Can delete category")
        ]


class Author(models.Model):
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    description = models.CharField("Об авторе", max_length=2500, default='Нету информации')

    img = models.ImageField("Изображение автора", upload_to='books/authors_images/', default='null')

    class Meta:
        # Указываем комбинацию полей, которая должна быть уникальной
        unique_together = ('name', 'surname')

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        permissions = [
            ("can_add_new_author", "Can add new author"),
            ("can_delete_author", "Can delete author")
        ]


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=2500)
    img = models.ImageField("Картинка", upload_to='books/books_images/')

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    publishing_house = models.ForeignKey('PublishingHouse', default='', on_delete=models.CASCADE, null=True)
    year_of_publishing = models.IntegerField("Год издания", default=2023)
    score = models.IntegerField("Рейтинг", default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])

    file = models.FileField('Файл', upload_to='books/file_books/% Y/% m/% d/')

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_new_book", "Can add new book"),
            ("can_delete_book", "Can delete book")
        ]
