from django.db import models


class Applications(models.Model):
    name = models.CharField(max_length=200)
    package = models.CharField(max_length=200)
    company = models.TextField(max_length=200)
    rating = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

