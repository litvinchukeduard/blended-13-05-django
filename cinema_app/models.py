from django.db import models

class Cinema(models.Model):
    name = models.CharField(null=False, max_length=255)
    location = models.TextField(null=False, max_length=255)
    capacity = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
