from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from .forms import DeportistaForm, ingresarform
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from .models import eventodeportivo

def index(request):
    consultaeventos=eventodeportivo.objects.all()
    return render(request,'home.html',{
                                    'eventos':consultaeventos
                                    })

def registrarse(request):
    if request.method == 'GET':
        return render(request,'registrarse.html',{'form':DeportistaForm})
        ##return render(request,'registrarse.html',{'form':UserCreationForm})
        ##print('entrando if')
        ##return render(request,'registrarse.html',{'form':RegistroForm})
    
    else:
       try: 
            form=DeportistaForm(request.POST,request.FILES)
            form.save()
            ##print(request.POST['usuario'])
            ##print(request.POST['clave'])
            user = User.objects.create_user(
                username=request.POST['usuario'],
                password=request.POST['clave'],
                is_staff=False
            )
            user.save()
            login(request,user)
            ##return render(request,'home.html')
            return redirect('home')
       except IntegrityError:
           return render(request,'registrarse.html',{
               'form':DeportistaForm,
               'error':'Usuario o cédula ya existente'})
       except ValueError:
           return render(request,'registrarse.html',{
               'form':DeportistaForm,
               'error':'Ingrese datos correctos y no repetidos(cédula o usuario)'})
        

def salirsesion(request):
    logout(request)
    return redirect('home')

def ingresar(request):
    if request.method == 'GET':
        return render(request,'ingresar.html',{'form':ingresarform})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'ingresar.html',{
                                'form':ingresarform,
                                'error':'Usuario o contraseña incorrectos'
                                                 })    
        else:
            ##return render(request,'ingresar.html',{'form':ingresarform})
            login(request, user)
            return redirect('home') 