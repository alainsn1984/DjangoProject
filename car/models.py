from django.db import models

# Create your models here.


class Cars(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    weight = models.PositiveIntegerField()