# crop_monitoring_app/models.py
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=255)
    def _str_(self):
        return self.name 

class CropPrice(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class Price(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
