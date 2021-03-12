from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    rating = models.FloatField(default=0)
    release_date = models.PositiveIntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    desc = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.name
