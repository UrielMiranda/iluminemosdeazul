from django.db import models

# Create your models here.
class ArtistModel(models.Model):

    # Atributes
    name = models.CharField(blank=False, max_length=255)
    instagram =  models.CharField(blank=False, max_length=55)




class GaleryModel(models.Model):

     artist = models.ForeignKey(ArtistModel)

     name = models.CharField(blank=True, max_length=55)
     image = models.ImageField()


