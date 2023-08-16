from typing import Any
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

##from user import user
from .models import deportista

class DeportistaForm(ModelForm):
    class Meta:
        model=deportista
        ##geeks_field = forms.ImageField()

        ##fields='__all__'
        fields=['foto','tipodeportista',
                'sexo','tiposangre','ceduladeportista','apellidosdeportista', 'nombresdeportista',
                'fecnacdeportista','email','direcciondeportista','telefonofijo',
                'telefonomovil','usuario','clave']
        widgets ={
           
            'ceduladeportista': forms.TextInput(attrs={'class':'form-control',"size": 15,
                                                       'placeholder':'Cédula'}),
            'apellidosdeportista': forms.TextInput(attrs={'class':'form-control',
                                                       'placeholder':'Ambos apellidos'}),
            'nombresdeportista': forms.TextInput(attrs={'class':'form-control',
                                                       'placeholder':'Ambos nombres'}),                                           
            'direcciondeportista': forms.Textarea(attrs={'class':'form-control',
                                                         'rows': 5,
                                                         'placeholder':'Dirección'}),
         }

class ingresarform(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ingresarform, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeholder']='Contraseña'