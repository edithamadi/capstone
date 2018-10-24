from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='profile/')
    id_number = models.IntegerField()
    maritalstatus = models.CharField(max_length=30)
    cellphone = models.IntegerField()
    emailaddress =  models.EmailField(max_length=75)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=40)
    description = models.TextField()
    
