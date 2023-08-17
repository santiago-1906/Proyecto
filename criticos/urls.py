from django.urls import path
from . import views

urlpatterns = [
    path('restaurantes/', views.lista_restaurantes, name='lista_restaurantes'),
    path('criticos/', views.lista_criticos, name='lista_criticos'),
    path('agregar_restaurante/', views.agregar_restaurante, name='agregar_restaurante'),
    path('agregar_critico/', views.agregar_critico, name='agregar_critico'),
    path('restaurantes/<int:restaurante_id>/', views.detalle_restaurante, name='detalle_restaurante'),
    path('restaurantes/<int:restaurante_id>/eliminar/', views.eliminar_restaurante, name='eliminar_restaurante'),
    path('restaurantes/<int:restaurante_id>/editar/', views.editar_restaurante, name='editar_restaurante'),

    path('mi_informacion/', views.mi_informacion, name='mi_informacion'),
]