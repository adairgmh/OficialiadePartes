# from msilib.schema import ListView
from pyexpat import model
from typing import List
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from OPUsuario.models import Usuario
from OP.forms import RespuestaForm, RegistrarForm, AgregarForm, AreaForm
from OPUsuario.forms import CustomCreationForm
from .decorators import allowed_users
from .models import Archivo, Area
from django.contrib import messages
from django.views.generic import ListView, TemplateView, UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.http import FileResponse
from django.http import JsonResponse
import io




class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'    

class AgregarUsuario(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Usuario
    template_name = 'registration/registroUsuario.html'    
    form_class = CustomCreationForm
    success_url = reverse_lazy('registro')
    success_message = 'Se registro al Usuario correctamente'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Se registro al Usuario correctamente"
    
class Registrar(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Archivo
    form_class = AgregarForm
    template_name  = 'registrar.html'
    success_url = reverse_lazy('registrar')
    success_message = 'Se realizo el registro correctamente'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "El registro se ha realizado correctamente"

class AgregarArea(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'agregararea.html'
    success_url = reverse_lazy('agregar_area')
    success_message = 'Se agrega la nueva area correctamente'
    
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "El registro se ha realizado correctamente"

class Seguimientos(LoginRequiredMixin, ListView):   
    model = Archivo, Usuario
    template_name = 'seguimientos.html'
    

    def get_queryset(self) :
        if self.request.user.groups.filter(name="area"):
            queryset = Archivo.objects.filter(area_id = self.request.user.area_id)
            return queryset
        else: 
            self.request.user.groups.filter(name="admin")
            queryset = Archivo.objects.all()
            return queryset

class Reportes(LoginRequiredMixin, ListView):
    model = Archivo
    template_name = 'reportes.html'

     

class ResponderOficio(LoginRequiredMixin, UpdateView, ListView):
    model = Archivo
    form_class = RespuestaForm
    template_name = 'respuesta.html'
    success_url = reverse_lazy('seguimientos')

class ResponderO(LoginRequiredMixin, UpdateView, ListView):
    model = Archivo
    form_class = RespuestaForm
    template_name = 'respuesta.html'
    success_url = reverse_lazy('seguimientos')

    def post(self, request):
        form = RespuestaForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_img = form.save(commit=False)
            uploaded_img.file_data = form.cleaned_data['respuesta'].file.read()
            uploaded_img.save()
            return redirect('seguimientos')
        else:
            form = AgregarForm()
        return render(request, 'respuesta.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        form = AgregarForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_img = form.save(commit=False)
            uploaded_img.file_data = form.cleaned_data['file'].file.read()
            uploaded_img.save()
            return redirect('subir')
    else:
        form = AgregarForm()
    return render(request, 'registrar.html', {'form': form})
    

class upload_file(CreateView):
    model = Archivo
    form_class = AgregarForm
    template_name  = 'registrar.html'
    success_url = reverse_lazy('subir')
    
    def post(self, request):
        form = AgregarForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_img = form.save(commit=False)
            uploaded_img.file_data = form.cleaned_data['file'].file.read()
            uploaded_img.save()
            return redirect('subir')
        else:
            form = AgregarForm()
        return render(request, 'registrar.html', {'form': form})

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "El registro se ha realizado correctamente"


def download(request, pk):
    # this url is for download
    try:
        obj = Archivo.objects.get(pk=pk)
    except Archivo.DoesNotExist as exc:
        return JsonResponse({'status_message': 'No Resource Found'})
    get_binary = obj.file_data
    if get_binary is None:
        return JsonResponse({'status_message': 'Resource does not contian image'})
    if isinstance(get_binary, memoryview):
        binary_io = io.BytesIO(get_binary.tobytes())
    else:
        binary_io = io.BytesIO(get_binary)
    response = FileResponse(binary_io)
    response['Content-Type'] = 'application/x-binary'
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(pk) # You can set custom filename, which will be visible for clients.
    return response