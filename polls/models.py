from pyexpat import model
from django.db import models

# Create your models here.

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

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    run_medico = models.IntegerField()
    dv_medico = models.IntegerField()
    nombre_medico = models.CharField(max_length=25)
    apellido_medico = models.CharField(max_length=25)
    sexo_medico = models.CharField(max_length=1)
    edad_medico = models.IntegerField()

class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=25)
    fecha_elab_medicamento = models.DateField()
    fecha_venc_medicamento = models.DateField()
    cantidad_medicamento = models.IntegerField()

class Stock_actual(models.Model):
    id_stock_actual = models.AutoField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)

class Stock_llegada(models.Model):
    id_stock_llegada = models.AutoField(primary_key=True)
    fecha_llegada = models.DateField()
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)

class Receta_medica(models.Model):
    id_receta = models.AutoField(primary_key=True)
    prescripcion_receta = models.TextField(max_length=200)
    fecha_receta = models.DateField()
    id_medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    id_medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)
    run_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)

class Ficha_paciente(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    fecha_retiro = models.DateField()
    run_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    id_receta = models.ForeignKey('Receta_medica', on_delete=models.CASCADE)

class Farmaceutico(models.Model):
    id_farmaceutico = models.AutoField(primary_key=True)
    run_farmaceutico = models.IntegerField()
    dv_farmaceutico = models.IntegerField()
    nombre_farmceutico = models.CharField(max_length=25)
    apellido_farmaceutico = models.CharField(max_length=25)
    edad_farmaceutico = models.IntegerField()
    sexo_farmaceutico = models.CharField(max_length=1)
    id_stock_actual = models.ForeignKey('Stock_actual', models.SET_NULL, blank=True, null=True)
    id_stock_llegada = models.ForeignKey('Stock_llegada', models.SET_NULL, blank=True, null=True)
    id_ficha = models.ForeignKey('Ficha_Paciente', on_delete=models.CASCADE)