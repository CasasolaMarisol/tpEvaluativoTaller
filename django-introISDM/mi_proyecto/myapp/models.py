from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
