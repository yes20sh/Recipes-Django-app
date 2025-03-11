from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    name_recipe = models.CharField(max_length=100)
    description_recipe = models.TextField()
    image_recipe = models.ImageField(upload_to="recipe_image")
