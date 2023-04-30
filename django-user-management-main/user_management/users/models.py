from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)