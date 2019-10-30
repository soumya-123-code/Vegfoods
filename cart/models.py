from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""
    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""
        if not email:
            raise ValueError("Users must have an email address.")
        email = self.normalize_email(email).lower()
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff= True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin): 
    """Represents a user profile inside our system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    # Object manager is a class to manage the userprofile, giving it extra functionality

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name


    

class Category(models.Model):
    category_name = models.CharField(max_length=128)

    def __str__(self):
        return self.category_name



class Product(models.Model):
    name = models.CharField(max_length=128)
    image=models.ImageField(null=True, blank=True, upload_to="product_images")
    price=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name









    