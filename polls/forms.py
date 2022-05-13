from dataclasses import field
from django import forms
from .models import Entrega_medicamentos, Ficha_paciente, Personal, Receta_medica, Paciente, Medicamento

#Create your forms here

#Lista de tuplas

tipos = (
    ('is_farm', 'Farmaceutico'),
    ('is_med', 'Medico'),
    ('is_adm', 'Administrador')
)

lista_recetas = ()
lista_recetas = list(lista_recetas)
receta_medica = Receta_medica.objects.all()
for p in receta_medica:
    lista_recetas.append([p.id, str('Receta numero: ' + str(p.id))])
lista_recetas = tuple(lista_recetas)

lista_fichas = ()
lista_fichas = list(lista_fichas)
ficha = Ficha_paciente.objects.all()
for p in ficha:
    lista_fichas.append([p.id, str('Ficha del tipo: ' + p.tipo_ficha)])
lista_fichas = tuple(lista_fichas)

lista_personal = ()
lista_personal = list(lista_personal)
personal = Personal.objects.all()
for p in personal:
    lista_personal.append([p.id, str(p.nombre_personal + ' ' + p.apellido_personal)])
lista_personal = tuple(lista_personal)

lista_medicamentos = ()
lista_medicamentos = list(lista_medicamentos)
medicamento = Medicamento.objects.all()
for m in medicamento:
    lista_medicamentos.append([m.id, str(m.nombre_medicamento)])
lista_medicamentos = tuple(lista_medicamentos)

lista_pacientes = ()
lista_pacientes = list(lista_pacientes)
paciente = Paciente.objects.all()
for p in paciente:
    lista_pacientes.append([p.id, str(p.nombre_paciente + ' ' + p.apellido_paciente)])
lista_pacientes = tuple(lista_pacientes)

#Creacion_personal
class creacion_personal(forms.Form):
    run_personal = forms.CharField(max_length=8)
    dv_personal = forms.CharField(max_length=1)
    nombre_personal = forms.CharField(max_length=25)
    apellido_personal = forms.CharField(max_length=25)
    mail_personal = forms.EmailField()
    sexo_personal = forms.CharField(max_length=1)
    edad_personal = forms.CharField(max_length=3)
    tipo = forms.ChoiceField(choices=tipos)

    class Meta:
        model = Personal, 
        fields = ['run_personal', 'dv_personal', 'nombre_personal', 'apellido_personal',
        'mail_personal', 'sexo_personal', 'edad_personal', 'tipo']

#Creacion Receta
class creacion_receta(forms.Form):
    prescripcion_receta = forms.CharField(max_length=200)
    fecha_receta = forms.DateField()
    cantidad_medicamentos = forms.CharField(max_length=4)
    id_personal = forms.ChoiceField(choices=lista_personal)
    id_medicamento = forms.ChoiceField(choices=lista_medicamentos)
    id_paciente = forms.ChoiceField(choices=lista_pacientes)

    class Meta:
        model = Receta_medica,
        fields = ['prescripcion_receta', 'fecha_receta', 'cantidad_medicamentos','id_personal', 'id_medicamento', 'id_paciente']



#Modificar stock
class modificar_stock(forms.Form):
    nombre_medicamento = forms.CharField(max_length=25, required=False)
    fecha_elab_medicamento = forms.DateField(required=False)
    fecha_venc_medicamento = forms.DateField(required=False)
    cantidad_medicamento = forms.CharField(max_length=4, required=False)

    class Meta:
        model = Medicamento,
        fields = ['nombre_medicamento', 'fecha_elab_medicamento', 'fecha_venc_medicamento', 'cantidad_medicamento']

#Entrega Medicamento
class entrega_medicamento(forms.Form):
    id_medicamento = forms.ChoiceField(choices=lista_medicamentos)
    cant_entregada = forms.CharField(max_length=4)
    id_ficha = forms.ChoiceField(choices=lista_fichas)
    id_personal = forms.ChoiceField(choices=lista_personal)
    id_receta = forms.ChoiceField(choices=lista_recetas)

    class Meta:
        model = Entrega_medicamentos,
        fields = ['cant_entregada', 'id_ficha', 'id_personal', 'id_receta']