from django.db import models
from musician.models import Musician


# Create your models here.
class Album(models.Model):
    RATING_CHOICES = [
        (1, "1 - Star"),
        (2, "2 - Star"),
        (3, "3 - Star"),
        (4, "4 - Star"),
        (5, "5 - Star"),
    ]

    name = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name
