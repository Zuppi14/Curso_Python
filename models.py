from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
    

#Cascade: eliminar el producto
#Protect: lanza error
#Restrict: solo elimina si no existen productos
#Set_Null: actualiza el valor a nulo
#Set_Default: asigna el valor por defecto


class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre