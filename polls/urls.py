from os import stat
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)