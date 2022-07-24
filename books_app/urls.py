from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_all_books, name='books'),
    path('<int:book_id>/', views.display_book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>', views.delete_book, name='delete_book'),
]
