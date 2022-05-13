from os import stat
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('admin_creacion/', views.admin_creacion, name='admin_creacion'),
    path('farm_home/', views.farm_home, name='farm_home'),
    path('farm_revisar_receta/', views.farm_revisar_receta, name='farm_revisar_receta'),
    path('farm_modificar_stock/', views.farm_modificar_stock, name='farm_modificar_stock'),
    path('medico_home/', views.medico_home, name='medico_home'),
    path('medico_receta_medica/', views.medico_receta_medica, name='medico_receta_medica'),
    path('desconectar/', views.desconectar, name= 'desconectar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)