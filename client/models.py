from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    pass

class Client(models.Model):

    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    order_name = models.TextField(default=0)
    total = models.IntegerField(default=0)
    seamstress = models.ForeignKey("Seamstress", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.second_name
    
class Seamstress(models.Model):
    class Meta:
        verbose_name = "Seamstress"
        verbose_name_plural = "Seamstresses"

    name = models.CharField(max_length=20)
    order_time = models.TimeField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name