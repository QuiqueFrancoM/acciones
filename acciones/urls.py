from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('todas/', views.lista_acciones, name='lista_acciones'),
    path('<int:id>/', views.accion_numero, name='accion_numero'),
    path('<str:nombre>/', views.accion_nombre, name='accion_nombre'),
]