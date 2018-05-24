from django.conf import settings
from django.db import models


class News(models.Model):
    content = models.CharField(max_length=120)
    # date = models.DateField()
    # title = models.CharField(max_length=120)
    # link = models.CharField(max_length=120)
    # Source = models.CharField(max_length=120)

class HimalayanTimes(models.Model):
    source = models.CharField(max_length=120, default='HimalayanTimes')
    date = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=120)
