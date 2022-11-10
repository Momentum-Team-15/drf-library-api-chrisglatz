from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.book_list, name='book_list.as_view'()),
    path('notes/', views.NoteList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
