from tabnanny import verbose
from django.db import models
from ntpath import join
from time import strftime
import random
import string
from datetime import datetime
import locale


# Create your models here.


class Area(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(null=True, max_length=100)
    #responsable foreign key
    
    def __str__(self):
        return self.nombre

def random_id(lenght=9):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(lenght))

def clave():
    mes = datetime.now().month
    mes = strftime("%b")

    return  mes

class Archivo(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.ForeignKey(Area, max_length=100, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    prioridad = models.CharField(max_length=100)
    fechar = models.CharField(max_length=100)
    fechao = models.CharField(max_length=100)
    procedencia = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=100)
    asunto = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    solicitante = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    recibio = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    file = models.FileField()
    file_data = models.BinaryField(null=True)
    respuesta = models.FileField()
    respuesta_data = models.BinaryField(null=True)
    status = models.BooleanField(default=False)
    folio = models.CharField(max_length=50, default=clave)

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivo'
        db_table = 'archivos'


