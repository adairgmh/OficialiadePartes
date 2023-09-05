import fileinput
from pickle import TRUE
from tkinter import Widget
from typing import Text
from django.forms import DateInput, FileField, ModelForm, SelectDateWidget, TextInput, Textarea
from OP.models import Archivo
from django import forms
from OP.models import Area


class RegistrarForm(forms.ModelForm):

    area = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}))

    TIPO_CHOICES = [('Conocimiento','Conocimiento'),('Solicitud','Solicitud'),('Requerimientos','Requerimientos')]
    tipo = forms.ChoiceField(choices=TIPO_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))

    PROCEDENCIA_CHOICES = [('Local','Local'),('Municipal','Municipal'),('Estatal','Estatal'),('Federal','Federal')]
    procedencia = forms.ChoiceField(choices=PROCEDENCIA_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))

    PRIORIDAD_CHOICES = [('Alta','Alta'),('Media','Media'),('Baja','Baja')]
    prioridad = forms.ChoiceField(choices=PRIORIDAD_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))

    fechar = forms.CharField(widget=DateInput(attrs={'type':'date','class':'form-control'}))

    fechao = forms.CharField(widget=DateInput(attrs={'type':'date','class':'form-control'}))

    DEPENDENCIA_CHOICES = [('Dep1','Dep1'),('Dep2','Dep2'),('Dep3','Dep3'),('Dep4','Dep4')]
    dependencia = forms.ChoiceField(choices=DEPENDENCIA_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
 
    solicitante = forms.CharField(widget=TextInput(attrs={'class':'form-control','type':'text'}))

    lugar = forms.CharField(widget=TextInput(attrs={'class':'form-control','type':'text'}))

    asunto = forms.CharField(widget=TextInput(attrs={'class':'form-control','type':'text'}))   

    telefono = forms.CharField(widget=TextInput(attrs={'class':'form-control','type':'tel'}))   
 
    recibio = forms.CharField(widget=TextInput(attrs={'class':'form-control','type':'text'}))   

    observaciones = forms.CharField(widget=Textarea(attrs={'class':'form-control','type':'text'}))   

    file = forms.FileField()


    class Meta:
        model = Archivo
        fields = ['area','tipo','procedencia','prioridad','fechar','fechao','dependencia','solicitante','lugar','asunto','telefono','recibio','observaciones','file' ]



class AgregarForm(forms.ModelForm):

    TIPO_CHOICES = [('Conocimiento','Conocimiento'),('Solicitud','Solicitud'),('Requerimientos','Requerimientos')]
    tipo = forms.ChoiceField(choices=TIPO_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))

    PROCEDENCIA_CHOICES = [('Local','Local'),('Municipal','Municipal'),('Estatal','Estatal'),('Federal','Federal')]
    procedencia = forms.ChoiceField(choices=PROCEDENCIA_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))

    PRIORIDAD_CHOICES = [('Alta','Alta'),('Media','Media'),('Baja','Baja')]
    prioridad = forms.ChoiceField(choices=PRIORIDAD_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))


    class Meta:
        model = Archivo

        fields = [
            'area',
            'tipo',
            'prioridad',
            'fechar',
            'fechao',
            'procedencia',
            'dependencia',
            'asunto',
            'lugar',
            'solicitante',
            'telefono',
            'recibio',
            'observaciones',
            'file'
            ]

        widgets = {
            
            'area': forms.Select(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'prioridad': forms.Select(attrs={'class':'form-control'}),
            'fechar': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'fechao': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'procedencia': forms.Select(attrs={'class':'form-control'}),
            'dependencia': forms.TextInput(attrs={'class':'form-control'}),
            'asunto': forms.TextInput(attrs={'class':'form-control'}),
            'lugar': forms.TextInput(attrs={'class':'form-control'}),
            'solicitante': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'recibio': forms.TextInput(attrs={'class':'form-control'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),
            'file': forms.FileInput(),
        }

class RespuestaForm(forms.ModelForm):
    
    statusc = [
    ('True','Atendido'),
    ('False','Pendiente')
    ]
    status = forms.ChoiceField(choices=statusc,widget=forms.RadioSelect)



    class Meta:
        model = Archivo
        fields = [
            'id',
            'status',
            'respuesta'
            ]
        
        labels = {
            'id':'id',
            'status':'status:',
            'respuesta':'Respuesta'
        }
        widgets = {
            'respuesta': forms.FileInput(attrs={'class':'form-control'}),
        }

class AreaForm(forms.ModelForm):
    
    nombre = forms.CharField(widget=TextInput(attrs={'class':'form-control','type':'text'}))
    descripcion = forms.CharField(widget=Textarea(attrs={'class':'form-control','type':'text'}))

    class Meta:
        model = Area
        fields = '__all__'

        