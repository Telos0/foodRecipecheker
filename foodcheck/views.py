from django.shortcuts import render, get_object_or_404
from foodcheck.models import Food, FoodIngredients, Ingredients
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.utils import timezone
from django.db.models import Sum, Count, Max, Min, Avg

#form class 선언
class FoodForm(forms.Form):
    food_name = forms.CharField(max_length=200)

class FoodIngredientsForm(forms.Form):
    ingredients_name = forms.CharField(max_length=200)


#함수
def home(request):
    reg_food_list = Food.objects.all().order_by('-insdttm')
    context = {'reg_food_list': reg_food_list}
    return render(request, 'foodcheck/home.html', context)

def foodingredients(request, food_name):
    foodingredients_list = FoodIngredients.objects.filter(food = food_name)
    context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
    return render(request, 'foodcheck/foodingredients.html', context)

def regfood(request):
    return render(request, 'foodcheck/regfood.html')

def compare(request):
    return render(request, 'foodcheck/compare.html')

def get_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)


        if form.is_valid():
            new_food_name = form.cleaned_data['food_name']
            new_insdttm = timezone.now()

            old_food = Food.objects.filter(food_name = new_food_name)
            for food in old_food:
                if food.food_name is not None:
                    return render(request, 'foodcheck/regfood.html', {'error_message': "That is already exist"})
            #new food 정의
            new_Food = Food(food_name = new_food_name, insdttm = new_insdttm)
            new_Food.save()

            #redirect
            return render(request, 'foodcheck/regfoodingredients.html', {'new_food_name': new_food_name})
        else:
            reg_food_list = Food.objects.all().order_by('-insdttm')
            context = {'reg_food_list': reg_food_list}
            return render(request, 'foodcheck/home.html', context)
    else:
        reg_food_list = Food.objects.all().order_by('-insdttm')
        context = {'reg_food_list': reg_food_list}
    return render(request, 'foodcheck/home.html', context)

#음식레시피 초기등록화면에서 호출하여 레시피를 추가
def get_foodingredients(request, new_food_name):
    if request.method == 'POST':
        form = FoodIngredientsForm(request.POST)
        if form.is_valid():
            new_ingredients_name = form.cleaned_data['ingredients_name']
            new_insdttm = timezone.now()

            new_food_object = Food.objects.get(food_name = new_food_name)
            new_ingredients_object = Ingredients.objects.get(ingredients_name = new_ingredients_name)


            old_ingredients = FoodIngredients.objects.filter(food = new_food_object, ingredients = new_ingredients_object)
            for ingrediendts in old_ingredients:
                if ingrediendts.food is not None:
                    return render(request, 'foodcheck/regfoodingredients.html', {'new_food_name' : new_food_name, 'error_message': "That is already exist"})
            #new foodingredients 정의
            new_Foodingredients = FoodIngredients(food = new_food_object, ingredients = new_ingredients_object, insdttm = new_insdttm)
            new_Foodingredients.save()

            new_food_object.ingredients_count += 1
            new_food_object.save()

            foodingredients_list = FoodIngredients.objects.filter(food = new_food_name)
            #redirect
            return render(request, 'foodcheck/regfoodingredients.html', {'new_food_name': new_food_name, 'foodingredients_list': foodingredients_list})
        else:
            render(request, 'foodcheck/regfoodingredients.html', {'new_food_name': new_food_name})
    else:
        foodingredients_list = FoodIngredients.objects.filter(food=new_food_name)

    return render(request, 'foodcheck/regfoodingredients.html', {'new_food_name': new_food_name, 'foodingredients_list': foodingredients_list})

#음식레시피 수정화면에서 호출하여 레시피를 삭제
def del_foodingeredients(request, food_name):
    if request.method == 'POST':
        form = FoodIngredientsForm(request.POST)
        if form.is_valid():
            ingredients_name = form.cleaned_data['ingredients_name']

            food_object = Food.objects.get(food_name = food_name)
            ingredients_object = Ingredients.objects.get(ingredients_name = ingredients_name)


            FoodIngredients.objects.filter(food = food_object, ingredients = ingredients_object).delete()
            food_object.ingredients_count -= 1
            food_object.save()
            #redirect
            foodingredients_list = FoodIngredients.objects.filter(food=food_name)
            context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
            return render(request, 'foodcheck/foodingredients.html', context)
        else:
            foodingredients_list = FoodIngredients.objects.filter(food=food_name)
            context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
            render(request, 'foodcheck/foodingredients.html', context)
    else:
        foodingredients_list = FoodIngredients.objects.filter(food=food_name)
        context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
        return render(request, 'foodcheck/foodingredients.html', context)
    foodingredients_list = FoodIngredients.objects.filter(food=food_name)
    context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
    return render(request, 'foodcheck/foodingredients.html', context)

#음식레시피 수정화면에서 호출하여 레시피를 추가
def add_foodingredients(request, food_name):
    if request.method == 'POST':
        form = FoodIngredientsForm(request.POST)
        if form.is_valid():
            ingredients_name = form.cleaned_data['ingredients_name']
            insdttm = timezone.now()

            food_object = Food.objects.get(food_name = food_name)
            ingredients_object = Ingredients.objects.get(ingredients_name = ingredients_name)


            old_ingredients = FoodIngredients.objects.filter(food = food_object, ingredients = ingredients_object)
            for ingrediendts in old_ingredients:
                if ingrediendts.food is not None:
                    foodingredients_list = FoodIngredients.objects.filter(food=food_name)
                    context = {'foodingredients_list': foodingredients_list, 'food_name': food_name, 'error_message': "That is already exist"}
                    return render(request, 'foodcheck/foodingredients.html', context)
            #new foodingredients 정의
            new_Foodingredients = FoodIngredients(food = food_object, ingredients = ingredients_object, insdttm = insdttm)
            new_Foodingredients.save()

            food_object.ingredients_count += 1
            food_object.save()

            #redirect
            foodingredients_list = FoodIngredients.objects.filter(food=food_name)
            context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
            return render(request, 'foodcheck/foodingredients.html', context)
        else:
            foodingredients_list = FoodIngredients.objects.filter(food=food_name)
            context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
            return render(request, 'foodcheck/foodingredients.html', context)
    else:
        foodingredients_list = FoodIngredients.objects.filter(food=food_name)
        context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
        return render(request, 'foodcheck/foodingredients.html', context)

    foodingredients_list = FoodIngredients.objects.filter(food=food_name)
    context = {'foodingredients_list': foodingredients_list, 'food_name': food_name}
    return render(request, 'foodcheck/foodingredients.html', context)


def compare_foodingredients(request):
    print("POST data : ", request.POST.getlist("ingredients_name[]"))
    postdata_list = request.POST.getlist("ingredients_name[]")


    postdata_list_objects = []
    for x in postdata_list:
        postdata_list_objects.append(Ingredients.objects.get(ingredients_name=x))


    queryset = FoodIngredients.objects.filter(ingredients__in = postdata_list_objects).values("food").annotate(
        ingre_count = Count("ingredients")
    ).values('food', 'ingre_count')
    for data in queryset:

        print("data : ", data.get("food"), " count: ", data.get("ingre_count"), "food_count : ", Food.objects.get(food_name = data.get("food")).ingredients_count)

    return render(request, 'foodcheck/compare.html')