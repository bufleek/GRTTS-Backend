from typing import TYPE_CHECKING, Optional

from django.db import models

#avoiding circular imports with accounts.Models
if TYPE_CHECKING:
    from accounts.models import User


# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    latitude = models.DecimalField(decimal_places=15, max_digits=20, null=False, blank=False)
    longitude = models.DecimalField(decimal_places=15, max_digits=20, null=False, blank=False)
    geo_radius = models.DecimalField(decimal_places=12, max_digits=20, null=False, blank=False)
    
class TimeLog(models.Model):
    user: Optional["User"] = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)
