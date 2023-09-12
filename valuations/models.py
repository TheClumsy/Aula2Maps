from django.db import models
from locations.models import Space


class Valuation(models.Model):
    nom = models.ForeignKey(Space, on_delete=models.CASCADE)
    titol = models.CharField(max_length=100)
    valoracio = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.nom)
