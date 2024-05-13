from django.db import models

class Cinema(models.Model):
    name = models.CharField(null=False, max_length=255)
    location = models.TextField(null=False, max_length=255)
    capacity = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    duration = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
    
class Screening(models.Model):
    movie = models.ManyToManyField(Movie)
    cinema = models.ManyToManyField(Cinema)
    datetime = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.movie}, {self.cinema}, {self.datetime}"