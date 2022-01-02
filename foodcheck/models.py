from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=200, primary_key=True)
    ingredients_count = models.IntegerField(default=0)
    insdttm = models.DateTimeField('date insterted')

    def __str__(self):
        return self.food_name

class Ingredients(models.Model):
    ingredients_name = models.CharField(max_length=200, primary_key=True)
    # unit = models.ForeignKey(UnitMaster, on_delete=models.CASCADE)
    insdttm = models.DateTimeField('date insterted')

    def __str__(self):
        return self.ingredients_name

class FoodIngredients(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    insdttm = models.DateTimeField('date insterted')

# class UnitMaster(models.Model):
#     unit = models.CharField(max_length=20, primary_key=True)
#     insdttm = models.DateTimeField('date insterted')
#
#     def __str__(self):
#         return self.unit