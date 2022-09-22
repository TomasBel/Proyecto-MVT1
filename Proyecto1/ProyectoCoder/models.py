from django.db import models

class MiFamily(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fecha_nac = models.DateField()