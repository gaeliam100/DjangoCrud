from django.db import models

# Create your models here.
# Creamos una clase llamada Task
# ¿Qué es el parametro que recibe la clase Task?    
#/
# ¿Qué es models.Model?
#  models.Model es una clase que se encarga de definir la estructura de la tabla en la base de datos
# /#
class Task(models.Model):
    id=models.CharField(primary_key=True,max_length=250)
    title=models.CharField(max_length=250)
    completed =models.BooleanField(default=False)
    def __str__(self):
        return self.title