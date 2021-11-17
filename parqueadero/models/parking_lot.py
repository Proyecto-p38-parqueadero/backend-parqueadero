from django.db import models


class Parking(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    administrador = models.CharField("administrador", max_length=50)
    telefono = models.CharField("telefono", max_length=50)
    direccion = models.CharField("direccion", max_length=50)
    email    = models.EmailField('Email',   max_length=100)
    ciudad = models.CharField("ciudad", max_length=80)