from django.db import models


# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    latitude = models.DecimalField(decimal_places=15, max_digits=20, null=False, blank=False)
    longitude = models.DecimalField(decimal_places=15, max_digits=20, null=False, blank=False)
    geo_radius = models.DecimalField(decimal_places=12, max_digits=20, null=False, blank=False)
