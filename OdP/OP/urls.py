from django.contrib import admin
from django.urls import path

from .views import Home, registrar, Seguimiento, Respuesta, registrar_archivo

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', Home, name='index'),
    path('registrar/', registrar, name='registrar'),
    path('seguimientos/', Seguimiento, name='seguimientos'),
    path('respuesta/', Respuesta, name='respuesta'),
]
