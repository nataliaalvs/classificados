"""classificados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),
    path('', inicio, name='inicio'),
    path('listagem/', listagem, name='listagem'),
    path('busca/', busca, name='busca'),
    path('resbusca/', resbusca, name='resbusca'),
    path('sobre/', sobre, name='sobre'),
    path('detalhes/<int:id>', detalhes, name='detalhes'),
    path('form/', form, name='form'),
    path('create/', crud, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('login/', login, name= 'login'),
    path('account/', include('django.contrib.auth.urls')),
]
