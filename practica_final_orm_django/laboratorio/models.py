from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)  # Aseguramos que el nombre sea único
    ciudad = models.CharField(max_length=255)  # Nuevo campo ciudad
    pais = models.CharField(max_length=255)  # Nuevo campo pais
  
    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='director_general'
    )  # Un laboratorio solo puede tener un director general
    especialidad = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='productos'
    )  # Cada producto pertenece a un solo laboratorio
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def clean(self):
        # Validación: la fecha de fabricación debe ser posterior a 2015
        if self.f_fabricacion < date(2015, 1, 1):
            raise ValidationError('La fecha de fabricación debe ser a partir de 2015.')

    def __str__(self):
        return self.nombre
