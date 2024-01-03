from django.db import models


# Create your models here.
class Color(models.Model):
    title = models.CharField(max_length=60)
    color = models.CharField(max_length=7)
    rating = models.IntegerField()

    class Meta:
        ordering = ['title']
