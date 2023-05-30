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



import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('static/images/', filename)



class Annonce(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),

    ]

    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    nomanimal = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)





















# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     sexe = models.Choices = (('option1'),
#         ('option2'))
#     description = models.TextField()
#     race = models.CharField(max_length=200)
#     age = models.DecimalField(max_length=200)
#     prix = models.DecimalField(max_length=200)
#     image = models.ImageField(upload_to='products/')
