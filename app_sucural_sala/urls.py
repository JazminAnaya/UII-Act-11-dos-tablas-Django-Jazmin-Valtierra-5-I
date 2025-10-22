from django.urls import path
from . import views

app_name = 'app_sucural_sala'

urlpatterns = [
    path('', views.listar_sucursales, name='listar_sucursales'),
    path('sucursal/<int:sucursal_id>/', views.detalle_sucursal, name='detalle_sucursal'),
    path('crear/', views.crear_sucursal, name='crear_sucursal'),
    path('editar/<int:sucursal_id>/', views.editar_sucursal, name='editar_sucursal'),
    path('borrar/<int:sucursal_id>/', views.borrar_sucursal, name='borrar_sucursal'),
]