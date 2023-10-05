from django import forms
from .models import Author, Book, Category

from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    description = forms.CharField(
        label="Описание",
        max_length=2500,
        widget=forms.Textarea(),
    )

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'category': 'Категория',
            'author': 'Автор',
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

