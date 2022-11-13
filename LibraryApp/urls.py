from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.book_list, name='book_list.as_view'()),
    path('notes/', views.note_list()),
    path('book/', views.book_detail()),
    path('featured', views.featured_list()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
