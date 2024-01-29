from django.db import models
from django.contrib.auth.models import *

##Las clases en si tienen elementos comunes,
##pero a la vez varian en construccion, rendimiento y variables maximas alcanzables##

#Clase Bomba Centrifuga
class BCentri(models.Model):

    def __str__(self): 
        return f"{self.id} --- {self.modelo} --- {self.presion} --- {self.caudal}"

    modelo = models.CharField(max_length=40)
    materiales_carcaza = models.CharField(max_length=40)
    materiales_voluta = models.CharField(max_length=40)
    presion = models.IntegerField()
    caudal = models.IntegerField()
    altura = models.IntegerField()
    temp = models.IntegerField()

#Clase Bomba de tornillo
    
class BTornillo(models.Model):
    
    def __str__(self): 
        return f"{self.id} --- {self.modelo} --- {self.presion} --- {self.caudal}"

    modelo = models.CharField(max_length=40)
    materiales_carcaza = models.CharField(max_length=40)
    materiales_tornillo = models.CharField(max_length=40)
    presion = models.IntegerField()
    caudal = models.IntegerField()
    altura = models.IntegerField()
    temp = models.IntegerField()

#Clase Bomba de engranajes

class BEngranajes(models.Model):
    
    def __str__(self): 
        return f"{self.id} --- {self.modelo} --- {self.presion} --- {self.caudal}"

    modelo = models.CharField(max_length=40)
    materiales_carcaza = models.CharField(max_length=40)
    materiales_engranajes = models.CharField(max_length=40)
    presion = models.IntegerField()
    caudal = models.IntegerField()
    altura = models.IntegerField()
    temp = models.IntegerField()

class AvatarUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
