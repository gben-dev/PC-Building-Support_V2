from django.urls import path
from .views import home, hardware, armar_tu_pc, login_view, registro, cerrar_sesion
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('hardware/', hardware, name="hardware"),
    path('armar_tu_pc/', armar_tu_pc, name="armar_tu_pc"),
    path('ensambles/', views.ensambles, name='ensambles'),
    path('resultado/', views.resultado, name='resultado'),
    path('ensambles/editar/<int:ensamble_id>/', views.editar_ensamble, name='editar_ensamble'),
    path('ensambles/eliminar/<int:ensamble_id>/', views.eliminar_ensamble, name='eliminar_ensamble'),
    path('login/', login_view, name='login'),
    path('registro/', registro, name='registro'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]


