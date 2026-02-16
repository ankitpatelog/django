from django.db import models

# Create your models here.

class Students(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        
        
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#         return f"the dog name is {self.name} and age is {self.age}"
    
#     def details_dog(self):
#         return f"the dog named{self.naem} is going to die at the the age of {self.age +5}"
        
    
# # now print the dog by making dew objects of class dog
# dog1 = Dog("baaku",10)
# dog2 = Dog("not baaku" , 9)

# print(dog1)
        