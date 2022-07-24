from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_all_authors, name='authors'),
    path('<int:author_id>/', views.display_author_detail,
         name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path('edit_author/<int:author_id>/', views.edit_author,
         name='edit_author'),
    path('delete_author/<int:author_id>', views.delete_author,
         name='delete_author'),
]
