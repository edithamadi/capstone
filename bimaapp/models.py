from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='profile/')
    maritalstatus = models.CharField(max_length=30)
    cellphone = models.IntegerField()
    emailaddress =  models.EmailField(max_length=75)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=40)
    description = models.TextField()

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

class premiumpaymethod(models.Model):
    name = models.CharField(max_length = 100)
    paymethod = (
        ('Mpesa Paybill', 'Mpesa Paybill'),
        ('Cheque Payments', 'Cheque Payments'),
        ('Check-off', 'Check-off'),
        ('Direct Debit', 'Direct Debit'),
    )

class Bankers_Order(models.Model):
    bank_name = (
        ('Equity Bank', 'Equity Bank'),
        ('Standard Chartered Bank', 'Standard Chartered Bank'),
        ('Kenya Commercial Bank', 'Kenya Commercial Bank'),
        ('Barclays', 'Barclays'),
    )
    branch_name = name = models.CharField(max_length = 100)
    account_name = models.PositiveIntegerField()
    account_number = models.ForeignKey(User, on_delete=models.CASCADE)

