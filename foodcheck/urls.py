from django.urls import path
from . import views

app_name = 'foodcheck'
urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('foodingeredientslist/<str:food_name>/', views.foodingredients, name='foodingredients'),
    path('regfood/', views.regfood, name='regfood'),
    path('compare/', views.compare, name='compare'),
    path('compare/compare_foodingredients/', views.compare_foodingredients, name='compare_foodingredients'),
    path('regfood/get_food/', views.get_food, name='regfood_new'),
    path('regfood/get_foodingredients/<str:new_food_name>/', views.get_foodingredients, name='regfoodingredients_new'),
    path('regfood/add_foodingredients/<str:food_name>/', views.add_foodingredients, name='add_regfoodingredients'),
    path('foodingeredientslist/del_foodingeredients/<str:food_name>/', views.del_foodingeredients, name='del_foodingeredients'),

]