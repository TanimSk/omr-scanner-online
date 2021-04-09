from django.db import models


class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    amount = models.IntegerField()


