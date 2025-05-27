from django.contrib.gis.db import models

# Create your models here.

#modello che corrisponde alla tabella dei punti di interesse
#ha un nome, descrizione ed il punto
class PointOfInterest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.PointField()

    def __str__(self):
        return self.name
