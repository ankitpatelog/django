from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=70)
    email=models.models.EmailField( max_length=254)  
    city=models.CharField(max_length=50)
    roll = models.models.IntegerField()  
    
# python manage.py makemigrations
# python manage.py migrate