from django.shortcuts import render, redirect
from .models import Entrega_medicamentos, Entrega_pendiente, Paciente, CustomUsuario, Personal, Medicamento, Receta_medica
from django.contrib.auth import authenticate, login, logout
from .forms import creacion_personal, creacion_receta, modificar_stock
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
import pywhatkit as pwk

# Create your views here.

#Identificacion ------------------------------------------------------------------

def iniciar_sesion(request):
    if request.user.is_authenticated and request.user.is_medico:
        return redirect(medico_home)
    elif request.user.is_authenticated and request.user.is_farmaceutico:
        return redirect(farm_home)
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
                return redirect(farm_home)
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

def desconectar(request):
    logout(request)
    return redirect('iniciar_sesion')    




#Farmaceutico ------------------------------------------------------------------

def farm_home(request):
    buscar_paciente = request.GET.get('buscador_paciente')
    medicamento = Medicamento.objects.all()
    paciente = Paciente.objects.all()
    verif = False

    if buscar_paciente and Paciente.objects.filter(Q(run_paciente = buscar_paciente)):
        paciente = Paciente.objects.filter(Q(run_paciente = buscar_paciente))
        verif = True

    data = {
        'paciente':paciente, 
        'medicamento': medicamento, 
        'verif':verif
    }

    return render(request, 'farmaceutico/farm_home.html', data)

def farm_revisar_receta(request):
    buscar_receta = request.GET.get('buscador_receta')
    id_receta_oculta = request.GET.get('id_receta_oculta')
    medicamento = Medicamento.objects.all()
    receta = Receta_medica.objects.all()
    verif = False
    
    if buscar_receta and Receta_medica.objects.filter(Q(id = buscar_receta)):
        receta = Receta_medica.objects.filter(Q(id = buscar_receta))
        verif = True
    
    if Receta_medica.objects.filter(Q(id = id_receta_oculta)):
        receta_for = Receta_medica.objects.filter(Q(id = id_receta_oculta)) 
        for r in receta_for:
            if r.cantidad_medicamentos > r.id_medicamento.cantidad_medicamento:
                agendar = Entrega_pendiente(
                    estado = 'Aun no se realiza la entrega',
                    queda_stock = False,
                    id_receta = r.id
                )
                agendar.save()
            else:
                receta_upd = Receta_medica.objects.filter(Q(id = r.id))
                medic = Medicamento.objects.filter(Q(id = r.id_medicamento.id))

                cant_medic = r.id_medicamento.cantidad_medicamento
                cant_medic = int(cant_medic)
                cant_entr = r.cantidad_medicamentos
                cant_entr = int(cant_entr)
                cant_total_medic = cant_medic - cant_entr

                entrega = Entrega_medicamentos(
                    cantidad_entregada = str(cant_entr),
                    id_receta = r.id,
                )
                entrega.save()

                medic = medic.update(cantidad_medicamento = str(cant_total_medic))
                receta_upd = receta_upd.update(cantidad_medicamentos = '0')
        
    data = {
        'receta': receta, 
        'medicamento': medicamento, 
        'verif': verif
    }

    return render(request, 'farmaceutico/farm_revisar_receta.html', data)

def farm_modificar_stock(request):
    medicamento = Medicamento.objects.all()

    if request.POST:
        form_modificacion = modificar_stock(request.POST, request.FILES)
        if form_modificacion.is_valid:
            medicamento = Medicamento.objects.filter(id = form_modificacion.data.get('medicamento'))
            nombre = form_modificacion.data.get('nombre_medicamento')
            fecha_elab = form_modificacion.data.get('fecha_elab_medicamento')
            fecha_venc = form_modificacion.data.get('fecha_venc_medicamento')
            cantidad = form_modificacion.data.get('cantidad_medicamento')
            if nombre:
                medicamento.update(nombre_medicamento = nombre)
            if fecha_elab:
                medicamento.update(fecha_elab_medicamento = fecha_elab)
            if fecha_venc:
                medicamento.update(fecha_venc_medicamento = fecha_venc)
            if cantidad:
                medicamento.update(cantidad_medicamento = cantidad)

    for ep in Entrega_pendiente.objects.all():
        if int(ep.id_receta.id_medicamento.cantidad_medicamento) > int(ep.id_receta.cantidad_medicamentos):
            #Envio mail
            subject = 'Medicamento disponible'
            message = 'Le informamos que el medicamento: ' + ep.id_receta.id_medicamento.nombre_medicamento + ' ya se encuentra disponible, acerquese a su sucursal mas cercana para poder solicitarlo'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [ep.id_receta.id_paciente.mail_paciente])

            #Envio whatsapp
            telefono = ep.id_receta.id_paciente.numero_telefonico
            mensaje = 'Le informamos que el medicamento: ' + ep.id_receta.id_medicamento.nombre_medicamento + ' ya se encuentra disponible, acerquese a su sucursal mas cercana para poder solicitarlo'
            pwk.sendwhatmsg_instantly(telefono, mensaje, wait_time=10)

            #Eliminacion
            #entr_p = Entrega_pendiente.objects.filter(id = ep.id)
            #entr_p.delete()


    medicamento = Medicamento.objects.all()

    data = {
        'form_modificacion': modificar_stock,
        'medicamento': medicamento,
    }
    return render(request, 'farmaceutico/farm_modificar_stock.html', data)




#Medico ------------------------------------------------------------------

def medico_home(request):
    buscar_paciente = request.GET.get('buscador_paciente')
    medicamento = Medicamento.objects.all()
    paciente = Paciente.objects.all()
    verif = False

    if buscar_paciente and Paciente.objects.filter(Q(run_paciente = buscar_paciente)):
        paciente = Paciente.objects.filter(Q(run_paciente = buscar_paciente))
        verif = True

    data = {
        'paciente':paciente, 
        'medicamento': medicamento, 
        'verif':verif
    }

    return render(request, 'medico/medico_home.html', data)

def medico_receta_medica(request):
    if request.POST:
        form = creacion_receta(request.POST, request.FILES)
        if form.is_valid():
            personal = Personal.objects.filter(Q(id = form.cleaned_data.get('id_personal')))
            medicamento = Medicamento.objects.filter(Q(id = form.cleaned_data.get('id_medicamento')))
            paciente = Paciente.objects.filter(Q(id = form.cleaned_data.get('id_paciente')))
            for p in personal:
                for m in medicamento:
                    for pa in paciente:
                        receta_medica = Receta_medica(prescripcion_receta = form.cleaned_data.get('prescripcion_receta'),
                        fecha_receta = form.cleaned_data.get('fecha_receta'),
                        cantidad_medicamentos = form.data.get('cantidad_medicamentos'),
                        id_personal = p,
                        id_medicamento = m,
                        id_paciente = pa
                        )
            receta_medica.save()
        return redirect(medico_home)
    
    data = {
        'form': creacion_receta,
    }
        
    return render(request, 'medico/medico_receta_medica.html', data)




#Creacion Admin ------------------------------------------------------------------

def admin_creacion(request):
    if request.POST:
        form = creacion_personal(request.POST, request.FILES)
        if form.is_valid():

            sexo_personal = form.data.get('sexo_personal')
            if sexo_personal == 'is_masc':
                personal = Personal(run_personal = form.cleaned_data.get('run_personal'),
                dv_personal = form.cleaned_data.get('dv_personal'),
                nombre_personal = form.cleaned_data.get('nombre_personal'),
                apellido_personal = form.cleaned_data.get('apellido_personal'),
                mail_personal = form.cleaned_data.get('mail_personal'),
                is_masculino = True,
                edad_personal = form.cleaned_data.get('edad_personal'),
                tipo = form.cleaned_data.get('tipo'))
            else:
                personal = Personal(run_personal = form.cleaned_data.get('run_personal'),
                dv_personal = form.cleaned_data.get('dv_personal'),
                nombre_personal = form.cleaned_data.get('nombre_personal'),
                apellido_personal = form.cleaned_data.get('apellido_personal'),
                mail_personal = form.cleaned_data.get('mail_personal'),
                is_femenino = True,
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

    return render(request, 'admin/admin_creacion.html', {'form': creacion_personal})