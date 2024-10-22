from django.db import models

# Create your models here.

class MoviesCreate(models.Model):
    title=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    review=models.TextField()

    def __str__(self):
        return self.title
    
class Theatre(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    screen_type=models.CharField(max_length=200)
    sound_system=models.CharField(max_length=200)
    seating=models.PositiveIntegerField()


