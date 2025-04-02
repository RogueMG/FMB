from django.db import models
from django.contrib.auth.models import User

class Tiffin(models.Model):
    tiffin_number = models.CharField(max_length=4)
    tiffin_mohalla = models.CharField(max_length=20)
    payment_status = models.BooleanField(null=True, blank=True,default=False)
    last_updated = models.DateTimeField(auto_now=True)
    incharge = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tiffins") #One incharge for all tiffins in an area or city, etc.

    def __str__(self):
        return self.tiffin_number