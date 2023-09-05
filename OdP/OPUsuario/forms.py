from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import widgets
from OPUsuario.models import Usuario


from django.contrib.auth.forms import UserCreationForm

class CustomCreationForm(UserCreationForm):
    
    pass
    class Meta: 
        model = Usuario
        fields = ('username','email','area', 'password1', 'password2',)

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'area' : forms.Select(attrs={'class':'form-control'}),
            'groups' : forms.Select(attrs={'class':'form-control'}),
            'password1' : forms.TextInput(attrs={'type':'password','class':'form-control'}),
            'password2' : forms.TextInput(attrs={'class':'form-control'}),
        
        }

