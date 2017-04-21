from django.db import models

# Create your models here.


class Mango(models.Model):
    """
    This model describes full specification for mangoes
    """

    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)