from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='profile/')
    maritalstatus = models.CharField(max_length=30,null=True)
    cellphone = models.IntegerField(null=True)
    emailaddress =  models.EmailField(max_length=75)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_user_profile(cls ,username):
        user = cls.objects.get(user = username)
        return user


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=40)
    description = models.TextField()
    def __str__(self):
        return f'{self.name}'


class Proposer(models.Model):

    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    dateofbirth = models.DateTimeField()
    id_number = models.IntegerField()
    maritalstatus = models.CharField(max_length=30)
    cellphone = models.IntegerField()
    emailaddress =  models.EmailField(max_length=75)
    relationshiptoassured = models.CharField(max_length=30)

class Lifeassured(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    dateofbirth  = models.DateField()
    nationality = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    agelastbirthday = models.CharField(max_length=30)
    maritalstatus = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)

class Address(models.Model):
    residentialname = models.CharField(max_length=30)
    workaddress = models.CharField(max_length=30)
    businessemail = models.EmailField(max_length=75)

class Occupation(models.Model):
    occupationname = models.CharField(max_length=30)
    annualincome = models.IntegerField()

class Premiumpaymethod(models.Model):
    name = models.CharField(max_length = 100)
    paymethodchoices = (
        ('Mpesa Paybill', 'Mpesa Paybill'),
        ('Cheque Payments', 'Cheque Payments'),
        ('Check-off', 'Check-off'),
        ('Direct Debit', 'Direct Debit'),
    )
    paymethod=models.CharField(max_length = 100 ,choices=paymethodchoices)

class Bankers_Order(models.Model):
    bank_namechoices = (
        ('Equity Bank', 'Equity Bank'),
        ('Standard Chartered Bank', 'Standard Chartered Bank'),
        ('Kenya Commercial Bank', 'Kenya Commercial Bank'),
        ('Barclays', 'Barclays'),
    )
    bank_name = models.CharField(max_length = 100, choices=bank_namechoices)
    branch_name = models.CharField(max_length = 100)
    account_name = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.PositiveIntegerField()
    
     
