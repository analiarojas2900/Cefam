from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from django.contrib.auth import authenticate, login

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
                return render(request, 'html/medico_receta_medica.html') #Temporal, cambiar cuando exista admin
            else:
                return redirect('registration/login.html')

        else:
            return redirect('registration/login.html')
    return render(request, 'registration/login.html')

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