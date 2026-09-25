"""
URL configuration for gallery_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. import:  from my_app import views
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
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from gallery import views as gallery_views  # gallery uygulamanın views dosyası

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Giriş ve Çıkış yolları (View'ı şişirmeyen Django formları)
    path('', auth_views.LoginView.as_view(authentication_form=AuthenticationForm, template_name='registration/login.html'), name='home'),
    path('login/', auth_views.LoginView.as_view(authentication_form=AuthenticationForm, template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Giriş yaptıktan sonra açılacak galeri/ana sayfa
    path('gallery/', gallery_views.home_view, name='gallery_home'),
    
    # Şifre Değiştirme Yolları (Django'nun dahili ve güvenli sistemi)
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='gallery/password_change.html', success_url='/gallery/password_change/done/'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='gallery/password_change_done.html'), name='password_change_done'),
]