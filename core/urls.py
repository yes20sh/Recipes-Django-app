"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path
from home.views import home
from home.views import success_page
from recipes.views import *

urlpatterns = [
    path ('', recipes, name="home"),
    path('admin/', admin.site.urls),
]

external_url = [
    path('success_page/', success_page, name="success Page"),
    path('recipes/', recipes, name = "My recipe app"),
    path('delete_recipe/<int:id>/', delete_recipe, name = "deleting the recipe"),
    path('update_recipe/<int:id>/', update_recipe, name = "update the recipe"),
    path('login/', login_page, name = "login page"),
    path('register/', register, name = "register page"),
    path('logout/', logout_page, name = "logout page")





]
urlpatterns += external_url

#  media file handling
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serves static files in development (optional)
urlpatterns += staticfiles_urlpatterns()
