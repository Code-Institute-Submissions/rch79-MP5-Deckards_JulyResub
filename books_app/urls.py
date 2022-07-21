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
    path('add_award/', views.add_award, name='add_award'),
    path('delete_award/<int:award_id>', views.delete_award, name='delete_award'),
    path('add_award_details/', views.add_award_details, name='add_award_details'),
    path('edit_award_detail/<int:award_detail_id>', views.edit_award_detail, name='edit_award_detail'),
    
]
