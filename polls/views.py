from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import creacion_personal

# Create your views here.

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_medico:
                login(request, user)
                return render(request, 'html/medico_home.html')
            elif user.is_farmaceutico:
                login(request, user)
                return render(request, 'html/farmaceutico_home.html')
            elif user.is_admin:
                login(request, user)
                return render(request, 'html/admin_creacion.html')  
            else:
                return redirect('registration/iniciar_sesion.html')

        else:
            return redirect('registration/iniciar_sesion.html')
    return render(request, 'registration/iniciar_sesion.html')

def farmaceutico_home(request):
    paciente = Paciente.objects.all()
    data = {
        'paciente': paciente,
    }
    return render(request, 'html/farmaceutico_home.html', data)

def farmaceutico_revisar_receta(request):
    return render(request, 'html/farmaceutico_revisar_receta.html')

def medico_home(request):
    return render(request, 'html/medico_home.html')

def medico_receta_medica(request):
    return render(request, 'html/medico_receta_medica.html')

def admin_creacion(request):
    if request.POST:
        nombre = ' '
        apellido = ' '
        run = ' '
        dv = ' '
        tipo = ' '
        form = creacion_personal(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre_personal')
            apellido = form.cleaned_data.get('apellido_personal')
            run = form.cleaned_data.get('run_personal')
            dv = form.cleaned_data.get('dv_personal')
            tipo = form.cleaned_data.get('tipo')
            if tipo == 'is_farm':
                User.username = nombre[0:2] + '.' + apellido
                User.password = apellido[0].capitalize() + str(run) + '-' + str(dv)
                User.is_farmaceutico = True
                User.save()
                form.save()
            elif tipo == 'is_med':
                User.username = nombre[0:2] + '.' + apellido
                User.password = apellido[0].capitalize() + str(run) + '-' + str(dv)
                User.is_medico = True
                User.save()
                form.save()
            elif tipo == 'is_adm':
                User.username = nombre[0:2] + '.' + apellido
                User.password = apellido[0].capitalize() + str(run) + '-' + str(dv)
                User.is_admin = True
                User.save()
                form.save()
        return render(request, 'admin_creacion')
    return render(request, 'html/admin_creacion.html', {'form': creacion_personal})

def desconectar(request):
    logout(request)
    return redirect('iniciar_sesion')