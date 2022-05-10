from django.contrib import admin
from .models import CustomUsuario, Entrega_medicamentos, Paciente, Medicamento, Personal, Receta_medica, Ficha_paciente

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Personal)
admin.site.register(Medicamento)
admin.site.register(Receta_medica)
admin.site.register(Ficha_paciente)
admin.site.register(CustomUsuario)
admin.site.register(Entrega_medicamentos)