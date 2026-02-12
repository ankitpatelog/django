from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# we made this in the top of the inbuilt userclass and added the two fiels
class CustomUser(AbstractUser):
    username = None  # remove username completeld
    # By setting username = None, we are completely removing the username field
    # Now this model will NOT expect username anymore

    email = models.EmailField(unique=True)
    # Email will be unique, so no two users can have same email

    birthday = models.DateField(null=True, blank=True)
    # birthday is optional (can be empty in DB and forms)

    USERNAME_FIELD = 'email'
    # This tells Django:
    # "Use email as the main login field instead of username"

    REQUIRED_FIELDS = []
    # When creating superuser, Django will only ask for:
    # email (USERNAME_FIELD) and password
    # No extra required fields

    objects = None  


# by doing so the carete superuser breakd as it expects the username not email 
# so we make the usermanager to hangle this issue and make login thorught email and password

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # self = the manager object
        # email and password come from form / terminal input

        if not email:
            raise ValueError('email is reqired')
            # If email not provided → stop and throw error

        email = self.normalize_email(email)
        # normalize_email converts ABC@GMAIL.COM → abc@gmail.com

        user = self.model(email=email, **extra_fields)
        # self.model = CustomUser
        # This line creates a new CustomUser object in memory

        user.set_password(password)
        # set_password hashes the password securely

        user.save(using=self._db)
        # Save user into database

        return user
        # Return created user object


    def create_superuser(self, email, password=None, **extra_fields):
        # This runs when we type:
        # python manage.py createsuperuser

        extra_fields.setdefault('is_staff', True)
        # Required for admin login

        extra_fields.setdefault('is_superuser', True)
        # Required for full admin permissions

        return self.create_user(email, password, **extra_fields)
        # Instead of rewriting logic, we reuse create_user()


# Now attach the manager properly
CustomUser.objects = CustomUserManager()
# Django automatically sets:
# CustomUser.objects.model = CustomUser
