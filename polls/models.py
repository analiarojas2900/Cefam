from contextlib import nullcontext
from pyexpat import model
from django.db import models

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

    def __str__(self):
        return self.run_paciente


#Medico
class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    run_medico = models.IntegerField()
    dv_medico = models.IntegerField()
    nombre_medico = models.CharField(max_length=25)
    apellido_medico = models.CharField(max_length=25)
    sexo_medico = models.CharField(max_length=1)
    edad_medico = models.IntegerField()

    def __str__(self):
        return self.id_medico


#Medicamento
class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=25)
    fecha_elab_medicamento = models.DateField()
    fecha_venc_medicamento = models.DateField()
    cantidad_medicamento = models.IntegerField()

    def __str__(self):
        return self.id_medicamento


#Stock_actual
class Stock_actual(models.Model):
    id_stock_actual = models.AutoField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.id_stock_actual


#Stock_llegada
class Stock_llegada(models.Model):
    id_stock_llegada = models.AutoField(primary_key=True)
    fecha_llegada = models.DateField()
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.id_stock_llegada


#Receta_medica
class Receta_medica(models.Model):
    id_receta = models.AutoField(primary_key=True)
    prescripcion_receta = models.TextField(max_length=200)
    fecha_receta = models.DateField()
    id_medico = models.ForeignKey('Medico', on_delete=models.CASCADE, default=None)
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE, default=None)
    run_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.id_receta


#Ficha_paciente
class Ficha_paciente(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    fecha_retiro = models.DateField()
    run_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, default=None)
    id_receta = models.ForeignKey('Receta_medica', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.id_ficha


#Farmaceutico
class Farmaceutico(models.Model):
    id_farmaceutico = models.AutoField(primary_key=True)
    run_farmaceutico = models.IntegerField()
    dv_farmaceutico = models.IntegerField()
    nombre_farmceutico = models.CharField(max_length=25)
    apellido_farmaceutico = models.CharField(max_length=25)
    edad_farmaceutico = models.IntegerField()
    sexo_farmaceutico = models.CharField(max_length=1)
    id_stock_actual = models.ForeignKey('Stock_actual', on_delete=models.CASCADE, default=None)
    id_stock_llegada = models.ForeignKey('Stock_llegada', on_delete=models.CASCADE, default=None)
    id_ficha = models.ForeignKey('Ficha_Paciente', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.id_farmaceutico