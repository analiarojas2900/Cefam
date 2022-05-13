from django.contrib import admin
from .models import CustomUsuario, CustomUsuarioAdmin, Entrega_medicamentos, Entrega_medicamentosAdmin, Ficha_pacienteAdmin, MedicamentoAdmin, Paciente, Medicamento, PacienteAdmin, Personal, PersonalAdmin, Ficha_paciente, Receta_medica, Receta_medicaAdmin

# Register your models here.

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Receta_medica, Receta_medicaAdmin)
admin.site.register(Ficha_paciente, Ficha_pacienteAdmin)
admin.site.register(CustomUsuario, CustomUsuarioAdmin)
admin.site.register(Entrega_medicamentos, Entrega_medicamentosAdmin)