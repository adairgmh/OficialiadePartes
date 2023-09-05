"""OdP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from OP import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from OPUsuario import views
from OP import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio.as_view(), name= "Home"),
    path('registrar', views.Registrar.as_view(), name="registrar"),
    path('respuesta/<int:pk>', views.ResponderOficio.as_view(),name="respuesta"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('seguimientos', views.Seguimientos.as_view(), name="seguimientos"),
    path('reportes', views.Reportes.as_view(), name="reportes"),
    path('registro', views.AgregarUsuario.as_view(), name="registro"),
    path('agregar_area', views.AgregarArea.as_view(), name="agregar_area"),
    path('download/<int:pk>/', views.download, name='download'),
    path('subir/', views.upload_file.as_view(), name='subir'),

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

