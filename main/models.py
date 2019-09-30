from django.db import models


class Asutus(models.Model):
  nimi = models.CharField(max_length = 255)

class Tootaja(models.Model):
  asutus = models.ForeignKey(Asutus, on_delete=models.CASCADE)
  eesNimi = models.CharField(max_length = 120)
  perekonnaNimi = models.CharField(max_length = 120)