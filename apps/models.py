from django.db import models


class Applications(models.Model):
    name = models.CharField(max_length=200)
    package = models.CharField(max_length=200)
    image = models.TextField()
    rating = models.CharField(max_length=200)
    position = models.IntegerField(default=0)
    careted_date = models.DateTimeField('date created')

