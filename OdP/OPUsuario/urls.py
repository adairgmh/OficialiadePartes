from django.urls import path
from django.contrib.auth.decorators import login_required
from OPUsuario.views import  registroview, registroCorrecto

urlpatterns = [
   
    #path('registrar_usuario/',RegistrarUser.as_view(),name='registrar_usuario'),
    path('registro/',registroview, name='registro'),
    path("registro_correcto/", registroCorrecto, name="registro_correcto")
]