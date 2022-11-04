from django.db import models

class Familia(models.Model):
    id=models.IntegerField().primary_key=True
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    parentesco=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField()
