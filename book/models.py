from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30, default='anonymus')
    email = models.EmailField(blank=True)
    picture = models.ImageField()
    describe = models.TextField(default='CRUD Django Tutorial')

    def __str__(self):
        return self.name # TODO