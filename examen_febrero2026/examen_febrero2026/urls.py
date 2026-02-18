"""
URL configuration for examen_febrero2026 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from socios.views import crear_disco, discos_lista
from publicaciones.views import crear_autor, autores_lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autor-create/', crear_autor.as_view(), name="autor-create"),
    path('autor-list/', autores_lista.as_view(), name="autor-list"),
    path('publicacion-create/', crear_disco.as_view(), name="publicacion-create"),
    path('publicacion-list/', discos_lista.as_view(),name="publicacion-list"),

]
