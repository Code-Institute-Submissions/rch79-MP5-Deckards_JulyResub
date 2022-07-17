from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_awards, name='awards'),
    path('<award_id>', views.award_detail, name='award_detail'),
]
