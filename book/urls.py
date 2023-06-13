from django.urls import path
from .views import index, upload, deleted_book, updated_book

app_name = 'book_app'

urlpatterns = [
    path('', index, name='index'),
    path('upload/', index, name='upload'),
    path('update/<int:book_id>', updated_book, name='update'),
    path('delete/<int:book_id>', deleted_book, name='delete'),
]