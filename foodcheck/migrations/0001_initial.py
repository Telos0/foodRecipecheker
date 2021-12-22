# Generated by Django 4.0 on 2021-12-18 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('insdttm', models.DateTimeField(verbose_name='date insterted')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('ingredients_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('insdttm', models.DateTimeField(verbose_name='date insterted')),
            ],
        ),
        migrations.CreateModel(
            name='FoodIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('insdttm', models.DateTimeField(verbose_name='date insterted')),
                ('food_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodcheck.food')),
                ('ingredients_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodcheck.ingredients')),
            ],
        ),
    ]