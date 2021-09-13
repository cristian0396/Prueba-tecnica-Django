import contextvars
from django.contrib.auth.forms import UsernameField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def Login(request):
    username = request.POST['username']
    return render(request, 'login.html', username)

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form' :form}
    return render(request, 'register.html', context)

def ShowChatHome(request):
    #username = request.POST['username']
    #context = {'user':username}
    return render(request,"chat_home.html")

def ShowChatPage(request, room_name, person_name):
    return render(request, "chat_screen.html",{'room_name':room_name, 'person_name':person_name})
    