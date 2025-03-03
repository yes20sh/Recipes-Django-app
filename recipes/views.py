from django.shortcuts import redirect, render
from recipes.models import *

# Create your views here.
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        # print(f"Name : {recipe_name} Desc : {recipe_description} image :  {recipe_image}")
        Recipe.objects.create(
            name_recipe = recipe_name,
            description_recipe = recipe_description,
            image_recipe = recipe_image
        )

        return redirect('/recipes/')
    
    data = Recipe.objects.all()
    if request.GET.get('search'):
        data = data.filter(name_recipe__icontains = request.GET.get('search'))

   
    context = {'recipes' : data}
    return render(request, "recipes.html", context)

# delete
def delete_recipe(request, id):
    recipe_del = Recipe.objects.get(id = id)
    recipe_del.delete()
    return redirect('/recipes/')

# updateing
def update_recipe(request, id):
    recipe_upd = Recipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        recipe_upd.name_recipe = recipe_name
        recipe_upd.description_recipe = recipe_description

        if  recipe_image:
            recipe_upd.image_recipe = recipe_image
        
        recipe_upd.save()

        return redirect('/recipes/')

    context = {'update_recipe' : recipe_upd}
    return render(request,'update_recipe.html', context)
