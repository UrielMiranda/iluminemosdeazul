from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return '%s' % self.name



class Affiliates(models.Model):

    AFFILIATES_SIZE = (
        ('1', 'Fundaciones'),
        ('2', 'Colaboradores'),
        ('3', 'Vocales'),
    )



    name = models.CharField(blank=False, max_length=255)
    link = models.CharField(blank=False, max_length=255)
    category = models.CharField(blank=False, max_length=1, choices=AFFILIATES_SIZE)
    phone = models.CharField(max_length=55)
    email = models.EmailField(default='')
    comment = models.TextField(default='')

    image = models.ImageField(upload_to='affiliates')
    published = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.name