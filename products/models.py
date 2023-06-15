from django.db import models

# Create your models here.

Rating = [
        
    ]


class Product(models.Model):
    class Rating(models.TextChoices):
        A = 'a', 'Average'
        B = 'b', 'Bad'
        E = 'e', 'Excellent'
    name = models.CharField(max_length=100)
    description = models.TextField()
    mfg_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=Rating.choices)

    def __str__(self):
        return self.name
    
    def show_desc(self):
        return self.description[:50]