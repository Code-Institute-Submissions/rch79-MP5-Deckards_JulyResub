from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='shopping_bag'),
    path('add/<book_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<book_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<book_id>/', views.remove_from_bag, name='remove_from_bag')
]
