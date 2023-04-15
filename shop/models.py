from django.db import models


class Shop(models.Model):
    """Shop model definition"""

    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200, blank=True, default="")
    tel = models.CharField(max_length=30, blank=True, default="")

    def __str__(self):
        return self.name
