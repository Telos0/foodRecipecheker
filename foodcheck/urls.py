from django.urls import path
from . import views

app_name = 'foodcheck'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:food_name>/', views.foodingredients, name='foodingredients'),
]