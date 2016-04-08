from django.db import models

# Create your models here.
class DirectorioModel(models.Model):

    name_institution = models.CharField(blank=False, max_length=255)
    url = models.CharField(blank=False, max_length=255)
    phone_institution = models.CharField(blank=False, max_length=55)
    person = models.CharField(blank=False, max_length=255)
    email = models.EmailField(blank=False)
    confirm_email = models.EmailField(blank=True)
    phone = models.CharField(blank=False, max_length=55)
    twitter = models.CharField(blank=True, max_length=255)
    facebook =  models.CharField(blank=True, max_length=255)
    linkedin = models.CharField(blank=True, max_length=255)
    instagram = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    num_external = models.CharField(blank=True, max_length=255)
    num_internal = models.CharField(blank=True, max_length=255)
    colony = models.CharField(blank=True, max_length=255)
    delegation_municipality = models.CharField(blank=True, max_length=255)
    postal_code = models.IntegerField()
    state = models.CharField(blank=True, max_length=255)
    #imagen = models.ImageField()