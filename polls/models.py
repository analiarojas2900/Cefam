from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Create your models here.

#Paciente
class Paciente(models.Model):
    run_paciente = models.CharField(max_length=8)
    dv_paciente = models.CharField(max_length=1)
    nombre_paciente = models.CharField(max_length=25)
    apellido_paciente = models.CharField(max_length=25)
    edad_paciente = models.CharField(max_length=4)
    is_masculino = models.BooleanField(default=False)
    is_femenino = models.BooleanField(default=False)
    direccion_paciente = models.CharField(max_length=60)
    mail_paciente = models.CharField(max_length=25)
    numero_telefonico = models.CharField(max_length=12)
    img_paciente = models.ImageField(upload_to='media')

    def __str__(self):
        return self.run_paciente

class PacienteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

#Personal
class Personal(models.Model):
    run_personal = models.CharField(max_length=8)
    dv_personal = models.CharField(max_length=1)
    nombre_personal = models.CharField(max_length=25)
    apellido_personal = models.CharField(max_length=25)
    mail_personal = models.EmailField()
    is_masculino = models.BooleanField(default=False)
    is_femenino = models.BooleanField(default=False)
    edad_personal = models.CharField(max_length=3)
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.run_personal

class PersonalAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    

#Medicamento
class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=25)
    fecha_elab_medicamento = models.DateField(null=True)
    fecha_venc_medicamento = models.DateField(null=True)
    cantidad_medicamento = models.CharField(max_length=4)

    def __str__(self):
        return self.nombre_medicamento

class MedicamentoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

#Receta_medica
class Receta_medica(models.Model):
    prescripcion_receta = models.CharField(max_length=200)
    fecha_receta = models.DateField()
    cantidad_medicamentos = models.CharField(max_length=4)
    id_personal = models.ForeignKey('Personal', on_delete=models.CASCADE)
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)

    def __str__(self):
        return self.prescripcion_receta

class Receta_medicaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

#CustomUsuario
class CustomUsuario(AbstractUser):
    is_medico = models.BooleanField(default=False)
    is_farmaceutico = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
class CustomUsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    
#Entrega Medicamentos
class Entrega_medicamentos(models.Model):
    cantidad_entregada = models.CharField(max_length=4)
    id_receta = models.ForeignKey('Receta_medica', on_delete=models.CASCADE)

    def __str__(self):
        return self.cantidad_entregada

class Entrega_medicamentosAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

#Entregas Pendientes
class Entrega_pendiente(models.Model):
    estado = models.CharField(max_length=50)
    queda_stock = models.BooleanField(default=True)
    id_receta = models.ForeignKey('Receta_medica', on_delete=models.CASCADE)

    def __str__(self):
        return self.estado

class Entrega_pendienteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)