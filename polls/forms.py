from django import forms
from .models import  Paciente, Personal, Receta_medica, Medicamento

#Create your forms here

#Lista de tuplas

tipos = (
    ('is_farm', 'Farmaceutico'),
    ('is_med', 'Medico'),
    ('is_adm', 'Administrador')
)

sexo = (
    ('is_masc', 'Masculino'),
    ('is_feme', 'Femenino')
)

#Colocar dentro de una funcion
def lista_personal():
    lista_personal = ()
    lista_personal = list(lista_personal)
    personal = Personal.objects.all()
    for p in personal:
        lista_personal.append([p.id, str(p.nombre_personal + ' ' + p.apellido_personal)])
    lista_personal = tuple(lista_personal)
    return lista_personal

def lista_medicamentos():
    lista_medicamentos = ()
    lista_medicamentos = list(lista_medicamentos)
    medicamento = Medicamento.objects.all()
    for m in medicamento:
        lista_medicamentos.append([m.id, str(m.nombre_medicamento)])
    lista_medicamentos = tuple(lista_medicamentos)
    return lista_medicamentos

def lista_pacientes():
    lista_pacientes = ()
    lista_pacientes = list(lista_pacientes)
    paciente = Paciente.objects.all()
    for p in paciente:
        lista_pacientes.append([p.id, str(p.nombre_paciente + ' ' + p.apellido_paciente)])
    lista_pacientes = tuple(lista_pacientes)
    return lista_pacientes

#Creacion_personal
class creacion_personal(forms.Form):
    run_personal = forms.CharField(max_length=8)
    dv_personal = forms.CharField(max_length=1)
    nombre_personal = forms.CharField(max_length=25)
    apellido_personal = forms.CharField(max_length=25)
    mail_personal = forms.EmailField()
    sexo_personal = forms.ChoiceField(choices=sexo)
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
    id_personal = forms.ChoiceField(choices=lista_personal())
    id_medicamento = forms.ChoiceField(choices=lista_medicamentos())
    id_paciente = forms.ChoiceField(choices=lista_pacientes())

    class Meta:
        model = Receta_medica,
        fields = ['prescripcion_receta', 'fecha_receta', 'cantidad_medicamentos','id_personal', 'id_medicamento', 'id_paciente']



#Modificar stock
class modificar_stock(forms.Form):
    medicamento = forms.ChoiceField(choices=lista_medicamentos(), required=True)
    nombre_medicamento = forms.CharField(max_length=25, required=False)
    fecha_elab_medicamento = forms.DateField(required=False)
    fecha_venc_medicamento = forms.DateField(required=False)
    cantidad_medicamento = forms.CharField(max_length=4, required=False)