from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    email = models.EmailField(max_length=70)
    city = models.CharField(max_length=70)

    # def __str__(self):  # Must be indented at same level as fields
    #     return self.name