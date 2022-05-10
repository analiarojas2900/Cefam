from contextlib import nullcontext
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#Paciente
class Paciente(models.Model):
    run_paciente = models.IntegerField(primary_key=True)
    dv_paciente = models.IntegerField()
    nombre_paciente = models.CharField(max_length=25)
    apellido_paciente = models.CharField(max_length=25)
    edad_paciente = models.IntegerField()
    sexo_paciente = models.CharField(max_length=1)
    direccion_paciente = models.CharField(max_length=60)
    mail_paciente = models.CharField(max_length=25)
    numero_telefonico = models.CharField(max_length=12)
    img_paciente = models.ImageField(upload_to='img_paciente', null=True)

#Personal
class Personal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    run_personal = models.IntegerField()
    dv_personal = models.IntegerField()
    nombre_personal = models.CharField(max_length=25)
    apellido_personal = models.CharField(max_length=25)
    mail_personal = models.EmailField()
    sexo_personal = models.CharField(max_length=1)
    edad_personal = models.IntegerField()
    tipo = models.CharField(max_length=25)
    

#Medicamento
class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=25)
    fecha_elab_medicamento = models.DateField()
    fecha_venc_medicamento = models.DateField()
    cantidad_medicamento = models.IntegerField()


#Receta_medica
class Receta_medica(models.Model):
    id_receta = models.AutoField(primary_key=True)
    prescripcion_receta = models.TextField(max_length=200)
    fecha_receta = models.DateField()
    id_medico = models.ForeignKey('Personal', on_delete=models.CASCADE, default=None)
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE, default=None)
    run_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, default=None)


#Ficha_paciente
class Ficha_paciente(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    fecha_retiro = models.DateField()
    run_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, default=None)
    id_receta = models.ForeignKey('Receta_medica', on_delete=models.CASCADE, default=None)
    

#CustomUsuario
class CustomUsuario(AbstractUser):
    is_medico = models.BooleanField(default=False)
    is_farmaceutico = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    
#Entrega Medicamentos
class Entrega_medicamentos(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    cantidad_entregada = models.IntegerField()
    id_ficha = models.ForeignKey('Ficha_paciente', on_delete=models.CASCADE)
    id_farmaceutico = models.ForeignKey('Personal', on_delete=models.CASCADE, default=None)
    id_receta = models.ForeignKey('Receta_medica', on_delete=models.CASCADE) 