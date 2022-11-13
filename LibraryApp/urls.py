from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.book_list()),
    path('notes/<int:pk>', views.note_list()),
    path('books/<int:pk>', views.book_detail()),
    path('featured', views.featured_list()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
