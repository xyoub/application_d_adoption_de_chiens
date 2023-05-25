# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    gmail = models.EmailField()

    def __str__(self):
        return self.nom

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     sexe = models.Choices = (('option1'),
#         ('option2'))
#     description = models.TextField()
#     race = models.CharField(max_length=200)
#     age = models.DecimalField(max_length=200)
#     prix = models.DecimalField(max_length=200)
#     image = models.ImageField(upload_to='products/')
