from django.db import models

class Profile(models.Model):
    name= models.models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    roll = models.models.IntegerField()
    
