"""
URL configuration for gallery_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.urls import path

# Geçici bir ana sayfa görünümü (İleride kendi galeri view'ın ile değiştirebilirsin)
def home_view(request):
    return HttpResponse("<h1>Galeri Ana Sayfasına Hoş Geldiniz!</h1><a href='/login/'>Giriş Yap</a>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]