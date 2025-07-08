from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect 


def register(request):
    if request.user.is_authenticated:
        return redirect('/posts/')  # Redirige si ya está logueado

    try:
        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Usuario creado exitosamente.')
                return redirect('login')
            else:
                messages.error(request, 'Por favor corrige los errores en el formulario.')
        else:
            form = RegistroForm()
    except Exception as e:
        # En producción no muestres el error; puedes loguearlo
        messages.error(request, 'Ocurrió un error inesperado. Intenta nuevamente.')
        form = RegistroForm()

    return render(request, 'accounts/register.html', {'form': form})



def index(request):
    return render(request,'index.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/posts/')

    try:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Bienvenido {username}")
                    return redirect('/posts/')
                else:
                    messages.error(request, 'Usuario o contraseña incorrectos')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            form = AuthenticationForm()
    except Exception as e:
        # Aquí podrías loguear el error si estás en modo desarrollo
        messages.error(request, 'Ocurrió un error inesperado. Intenta de nuevo.')
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
