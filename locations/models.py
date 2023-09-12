from django.db import models


class Space(models.Model):
    nom = models.CharField(max_length=100, primary_key=True)  # name of the space
    espai = models.CharField(max_length=100)  # ex: school, park, ...
    email = models.EmailField(max_length=200, null=True, blank=True)  # email of the space, if it exists
    telefon = models.CharField(max_length=100, null=True, blank=True)  # phone number of the space, if it exists
    web = models.URLField(max_length=500, null=True, blank=True)  # the web of the side, if it exists
    coordenades = models.CharField(max_length=100)  # coordinates

    def __str__(self):
        return self.nom
