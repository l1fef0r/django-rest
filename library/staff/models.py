from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64,  unique=True)
    birthday = models.PositiveIntegerField()
