from django.urls import path
from . import views
urlpatterns=[
    path('', views.Clientes ),  # Se define una ruta vacía como la raíz del sitio y la asocia a la vista llamada "Clientes"
]