from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('farmaceutico_home', views.farmaceutico_home, name='farmaceutico_home'),
    path('farmaceutico_revisar_receta', views.farmaceutico_revisar_receta, name='farmaceutico_revisar_receta'),
    path('medico_home', views.medico_home, name='medico_home'),
    path('medico_receta_medica', views.medico_receta_medica, name='medico_receta_medica'),
]