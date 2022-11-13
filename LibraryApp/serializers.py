from rest_framework import serializers
from LibraryApp.models import Book, Note


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'pubdate', 'is_featured']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['user', 'book', 'date_created', 'title', 'notes']
