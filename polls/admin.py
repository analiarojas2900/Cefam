from django.contrib import admin
from .models import Paciente, Medico, Medicamento, Stock_actual, Stock_llegada, Receta_medica, Ficha_paciente, Farmaceutico

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Medicamento)
admin.site.register(Stock_actual)
admin.site.register(Stock_llegada)
admin.site.register(Receta_medica)
admin.site.register(Ficha_paciente)
admin.site.register(Farmaceutico)