from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('delete_author/<int:author_id>', views.delete_author, name='delete_author'),
]
