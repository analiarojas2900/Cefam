from pyexpat import model
from django import forms
from .models import Personal

#Create your forms here

tipos = (
    ('', 'Elija su funcion'),
    ('is_farm', 'Farmaceutico'),
    ('is_med', 'Medico'),
    ('is_adm', 'Administrador')
)

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
