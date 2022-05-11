from re import template
from django.shortcuts import render, redirect
from .models import Paciente, CustomUsuario, Personal, Medicamento
from django.contrib.auth import authenticate, login, logout
from .forms import creacion_personal
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def iniciar_sesion(request):
    if request.user.is_authenticated and request.user.is_medico:
        return redirect(medico_home)
    elif request.user.is_authenticated and request.user.is_farmaceutico:
        return redirect(farmaceutico_home)
    elif request.user.is_authenticated:
        if request.user.is_admin or request.user.is_staff:
            return redirect(admin_creacion)
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_medico:
                login(request, user)
                return redirect(medico_home)
            elif user.is_farmaceutico:
                login(request, user)
                return redirect(farmaceutico_home)
            elif user.is_admin or user.is_staff:
                login(request, user)
                return redirect(admin_creacion)
            else:
                messages.success(request, 'No se logro verificar su usuario, intentelo nuevamente')
                return redirect(iniciar_sesion)
        else:
            messages.success(request, 'No se logro verificar su usuario, intentelo nuevamente')
            return redirect(iniciar_sesion)

    return render(request, 'registration/iniciar_sesion.html')

def farmaceutico_home(request):

    buscar_paciente = request.GET.get('buscador_paciente')
    medicamento = Medicamento.objects.all()

    if buscar_paciente:
        paciente = Paciente.objects.filter(Q(run_paciente = buscar_paciente))
    else:
        paciente = Paciente.objects.filter(Q(run_paciente = '1'))

    return render(request, 'html/farmaceutico_home.html', {'paciente':paciente, 'medicamento':medicamento})

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
            personal = Personal(run_personal = form.cleaned_data.get('run_personal'),
            dv_personal = form.cleaned_data.get('dv_personal'),
            nombre_personal = form.cleaned_data.get('nombre_personal'),
            apellido_personal = form.cleaned_data.get('apellido_personal'),
            mail_personal = form.cleaned_data.get('mail_personal'),
            sexo_personal = form.cleaned_data.get('sexo_personal'),
            edad_personal = form.cleaned_data.get('edad_personal'),
            tipo = form.cleaned_data.get('tipo'))
            nombre = form.cleaned_data.get('nombre_personal')
            apellido = form.cleaned_data.get('apellido_personal')
            run = form.cleaned_data.get('run_personal')
            dv = form.cleaned_data.get('dv_personal')
            tipo = form.cleaned_data.get('tipo')
            if tipo == 'is_farm':
                user = CustomUsuario.objects.create_user(username = nombre[0:2] + '.' + apellido,
                password = apellido[0].capitalize() + str(run) + '-' + str(dv),
                is_farmaceutico = True)
                user.save()
                personal.save()
            elif tipo == 'is_med':
                user = CustomUsuario.objects.create_user(username = nombre[0:2] + '.' + apellido,
                password = apellido[0].capitalize() + str(run) + '-' + str(dv),
                is_medico = True)
                user.save()
                personal.save()
            elif tipo == 'is_adm':
                user = CustomUsuario.objects.create_user(username = nombre[0:2] + '.' + apellido,
                password = apellido[0].capitalize() + str(run) + '-' + str(dv),
                is_admin = True)
                user.save()
                personal.save()
            messages.success(request, 'Usuario creado correctamente, su cuenta: \nnombre: ' + nombre[0:2] + '.' + apellido +
            '\ncontraseña: '+ apellido[0].capitalize() + str(run) + '-' + str(dv))
        return redirect(admin_creacion)
    return render(request, 'html/admin_creacion.html', {'form': creacion_personal})

def desconectar(request):
    logout(request)
    return redirect('iniciar_sesion')    