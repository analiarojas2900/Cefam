from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'registration/login.html')

def farmaceutico_home(request):
    return render(request, 'html/farmaceutico_home.html')

def farmaceutico_revisar_receta(request):
    return render(request, 'html/farmaceutico_revisar_receta.html')

def medico_home(request):
    return render(request, 'html/medico_home.html')

def medico_receta_medica(request):
    return render(request, 'html/medico_receta_medica.html')