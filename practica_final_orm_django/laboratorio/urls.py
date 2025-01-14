from django.urls import path
from .views import ver_laboratorios, agregar_laboratorio, editar_laboratorio, eliminar_laboratorio

urlpatterns = [
    # CRUD para Laboratorio
    path('', ver_laboratorios, name='laboratorio-list'),
    path('create/', agregar_laboratorio, name='laboratorio-create'),
    path('update/<int:pk>/', editar_laboratorio, name='laboratorio-update'),
    path('delete/<int:pk>/', eliminar_laboratorio, name='laboratorio-delete'),
]
