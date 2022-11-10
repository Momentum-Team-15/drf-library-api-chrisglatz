from rest_framework import serializers
from LibraryApp.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'pubdate', 'is_featured']
