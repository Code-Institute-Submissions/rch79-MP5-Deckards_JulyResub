from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_authors, name='authors'),
    path('<int:author_id>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path('delete_author/<int:author_id>', views.delete_author, name='delete_author'),
]
