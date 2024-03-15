from django.db import models
from django.urls import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.pk)])

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient-detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)

    ingredients = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name='recipe')
    
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='ingredient')
    
    def __str__(self):
        return '{}: {} '.format(self.ingredients,  self.quantity)
    
    


# Create your models here.
