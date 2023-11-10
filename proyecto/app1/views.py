from django.shortcuts import render
from .models import Cliente,Area,Empleado,Venta



def Clientes(request):
 
    clientes=Cliente.objects.all()
    area=Area.objects.all()
    empleado=Empleado.objects.all()
    venta=Venta.objects.all()

    return render(request, 'Clientes.html', {'clientes':clientes,'area':area,'empleado':empleado, 'venta':venta } )