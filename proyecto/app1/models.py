from django.db import models


class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.PositiveIntegerField(max_length=3)
    dui=models.PositiveIntegerField(max_length=9)
    
class Area(models.Model):
    nombre_del_area=models.CharField(max_length=50)
    descripcion=models.CharField()
    
class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.PositiveIntegerField(max_length=3)
    areaId=models.ForeignKey(Area, on_delete=models.CASCADE)

class Venta(models.Model):
    fecha_venta=models.DateTimeField()
    monto=models.FloatField()
    clienteId=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleadoId=models.ForeignKey(Empleado,on_delete=models.CASCADE)
    
    

    
