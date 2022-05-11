from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth.views import logout_then_login
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('farmaceutico_home/', views.farmaceutico_home, name='farmaceutico_home'),
    path('farmaceutico_revisar_receta/', views.farmaceutico_revisar_receta, name='farmaceutico_revisar_receta'),
    path('medico_home/', views.medico_home, name='medico_home'),
    path('medico_receta_medica/', views.medico_receta_medica, name='medico_receta_medica'),
    path('desconectar/', views.desconectar, name= 'desconectar'),
    path('admin_creacion/', views.admin_creacion, name='admin_creacion'),
]