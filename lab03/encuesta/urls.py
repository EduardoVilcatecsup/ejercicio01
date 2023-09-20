from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('venta/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    path('venta/<int:venta_id>/resultados/', views.resultados_venta, name='resultados_venta'),
]
