from django.shortcuts import redirect, render
from recipes.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
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
@login_required(login_url="/login/")
def delete_recipe(request, id):
    recipe_del = Recipe.objects.get(id = id)
    recipe_del.delete()
    return redirect('/recipes/')

# updateing
@login_required(login_url="/login/")
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

def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect("/login/")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("/login/")       
        
        else:
            login(request, user)
            return redirect("/recipes/")       

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username is already taken")
            return redirect("/register/")

        user = User.objects.create(
            username = username,
            first_name = full_name,
            email = email
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")

        return redirect('/register/')

    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect("/login/")


