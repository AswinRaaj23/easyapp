from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<slug>', views.posts_detail, name='posts_detail'),
    
]
