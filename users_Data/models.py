from importlib.resources import path
from django.db import models
class users(models.Model):
    name=models.TextField(max_length=100)
    file=models.TextField(max_length=300,default="hello")
    def __str__(self):
        return self.name