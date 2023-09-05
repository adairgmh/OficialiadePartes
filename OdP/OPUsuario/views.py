from django.shortcuts import redirect, render
from OPUsuario.forms import CustomCreationForm

# Create your views here.


def registroview(request):
    data ={
        'form':CustomCreationForm()
    }
    if request.method =='POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()  
            return redirect('usuarios:registro_correcto')
        data["form"]= formulario
    return render(request, 'registro/registro.html',data)


def registroCorrecto(request):
    return render(request, 'registro/registro_exitoso.html')

