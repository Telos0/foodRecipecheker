from django.contrib import admin

# Register your models here.
from foodcheck.models import Food, Ingredients, FoodIngredients

admin.site.register(Food)
admin.site.register(Ingredients)
admin.site.register(FoodIngredients)