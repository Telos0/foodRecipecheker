from django.shortcuts import render, get_object_or_404
from foodcheck.models import Food, FoodIngredients, Ingredients
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    reg_food_list = Food.objects.all().order_by('-insdttm')[:5]
    context = {'reg_food_list': reg_food_list}
    return render(request, 'foodcheck/home.html', context)

def foodingredients(request, food_name):
    foodingredients_list = FoodIngredients.objects.filter(food = food_name)
    context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
    return render(request, 'foodcheck/foodingredients.html', context)