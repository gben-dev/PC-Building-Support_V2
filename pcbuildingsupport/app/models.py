from django.db import models

# Create your models here.
class Ensamble(models.Model):
    procesador = models.CharField(max_length=100)
    memoria_ram = models.CharField(max_length=100)
    disco_duro = models.CharField(max_length=100)
    tarjeta_video = models.CharField(max_length=100)
    fuente_poder = models.CharField(max_length=100)
    
    def __str__(self):
        return self.procesador
    