from django.db import models

class Recipe(models.Model):
    name_recipe = models.CharField(max_length=100)
    description_recipe = models.TextField()
    image_recipe = models.ImageField(upload_to="recipe_image")
