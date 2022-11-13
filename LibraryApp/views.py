from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import Book, Note
from .serializers import BookSerializer, NoteSerializer


class book_list(generics.ListCreateAPIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class note_list(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Note.objects.filter(user=self.request.user)
        return queryset

class featured_list(generics.ListAPIView)
    queryset = Book.objects.filter(is_featured=True)
    serializer_class = Bookserializer

    def get_queryset(self):
        queryset = Book.objects.filter(is_featured=True)
        return queryset


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'library': reverse('library-list', request=request, format=format),
        'tracking': reverse('tracking-list', request=request, format=format),
        'notes': reverse('notes-list', request=request, format=format)
    })
