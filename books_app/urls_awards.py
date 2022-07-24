from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_all_awards, name='awards'),
    path('<int:award_id>/', views.display_award_detail, name='award_detail'),
    path('add_award/', views.add_award, name='add_award'),
    path('add_award_details/', views.add_award_details,
         name='add_award_details'),
    path('edit_award/<int:award_id>', views.edit_award, name='edit_award'),
    path('edit_award_detail/<int:award_detail_id>', views.edit_award_detail,
         name='edit_award_detail'),
    path('delete_award/<int:award_id>', views.delete_award,
         name='delete_award'),
    path('delete_award_detail/<int:award_detail_id>',
         views.delete_award_detail, name='delete_award_detail'),
]
