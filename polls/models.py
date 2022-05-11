from contextlib import nullcontext
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#Paciente
class Paciente(models.Model):
    run_paciente = models.CharField(max_length=8)
    dv_paciente = models.CharField(max_length=1)
    nombre_paciente = models.CharField(max_length=25)
    apellido_paciente = models.CharField(max_length=25)
    edad_paciente = models.IntegerField()
    sexo_paciente = models.CharField(max_length=1)
    direccion_paciente = models.CharField(max_length=60)
    mail_paciente = models.CharField(max_length=25)
    numero_telefonico = models.CharField(max_length=12)
    img_paciente = models.ImageField(upload_to='media')

    def __str__(self):
        return self.run_paciente

#Personal
class Personal(models.Model):
    run_personal = models.CharField(max_length=8)
    dv_personal = models.CharField(max_length=1)
    nombre_personal = models.CharField(max_length=25)
    apellido_personal = models.CharField(max_length=25)
    mail_personal = models.EmailField()
    sexo_personal = models.CharField(max_length=1)
    edad_personal = models.CharField(max_length=3)
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.run_personal
    

#Medicamento
class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=25)
    fecha_elab_medicamento = models.DateField()
    fecha_venc_medicamento = models.DateField()
    cantidad_medicamento = models.CharField(max_length=4)

    def __str__(self):
        return self.nombre_medicamento


#Receta_medica
class Receta_medica(models.Model):
    prescripcion_receta = models.TextField(max_length=200)
    fecha_receta = models.DateField()
    id_personal = models.ForeignKey('Personal', on_delete=models.CASCADE, default=None)
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE, default=None)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.prescripcion_receta


#Ficha_paciente
class Ficha_paciente(models.Model):
    tipo_ficha = models.CharField(max_length=25)
    fecha_retiro = models.DateField()
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, default=None)
    id_receta = models.ForeignKey('Receta_medica', on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.tipo_ficha

#CustomUsuario
class CustomUsuario(AbstractUser):
    is_medico = models.BooleanField(default=False)
    is_farmaceutico = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    
#Entrega Medicamentos
class Entrega_medicamentos(models.Model):
    tipo_entrega = models.CharField(max_length=25)
    cantidad_entregada = models.CharField(max_length=4)
    id_ficha = models.ForeignKey('Ficha_paciente', on_delete=models.CASCADE)
    id_personal = models.ForeignKey('Personal', on_delete=models.CASCADE, default=None)
    id_receta = models.ForeignKey('Receta_medica', on_delete=models.CASCADE) 

    def __str__(self):
        return self.tipo_entrega