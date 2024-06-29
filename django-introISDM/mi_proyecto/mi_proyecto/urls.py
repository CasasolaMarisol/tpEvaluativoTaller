"""mi_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mi_proyecto.views import agregar_persona, ver_personas, editar_persona, eliminar_persona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ver_personas/', ver_personas, name='ver_personas'),
    path('editar_persona/<int:persona_id>/', editar_persona, name='editar_persona'),
    path('eliminar_persona/<int:persona_id>/', eliminar_persona, name='eliminar_persona'),
    path('agregar_persona/', agregar_persona, name='agregar_persona'),
]
