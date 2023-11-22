from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu_items/', views.menu_items, name='menu_items'),
    path('register/', views.register_view, name='register'),
]