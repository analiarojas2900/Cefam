from django.contrib import admin
from .models import Entrega_medicamentos, Paciente, Medico, Medicamento, Receta_medica, Ficha_paciente, Farmaceutico, Usuario

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Medicamento)
admin.site.register(Receta_medica)
admin.site.register(Ficha_paciente)
admin.site.register(Farmaceutico)
admin.site.register(Usuario)
admin.site.register(Entrega_medicamentos)