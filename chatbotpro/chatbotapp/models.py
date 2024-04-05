from email import message
from django.db import models


# Create your models here.
class Thereg(models.Model):
    uname = models.CharField(max_length=200,null=True,blank=False)
    password = models.CharField(max_length=200,null=True,blank=False)
    location = models.CharField(max_length=200,null=True,blank=False)  
    email = models.CharField(max_length=200,null=True,blank=False)
    img = models.ImageField(upload_to='image',null=True,blank=False)

class Userreg(models.Model):
    uname = models.CharField(max_length=200,null=True,blank=False)
    gname = models.CharField(max_length=200,null=True,blank=False) 
    age = models.IntegerField(null=True,blank=False) 
    password = models.CharField(max_length=200,null=True,blank=False)
    number = models.IntegerField(null=True,blank=False)  
    location = models.CharField(max_length=200,null=True,blank=False)  
    email = models.CharField(max_length=200,null=True,blank=False)

class Docreg(models.Model):
    uname = models.CharField(max_length=200,null=True,blank=False)
    experience = models.CharField(max_length=200,null=True,blank=False) 
    qua = models.CharField(max_length=200,null=True,blank=False) 
    password = models.CharField(max_length=200,null=True,blank=False)
    number = models.IntegerField(null=True,blank=False)  
    location = models.CharField(max_length=200,null=True,blank=False)  
    email = models.CharField(max_length=200,null=True,blank=False) 

class labsaddreport(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=False) 
    drname=models.CharField(max_length=200,null=True,blank=False) 
    number = models.IntegerField(null=True,blank=False) 
    age = models.IntegerField(null=True,blank=False)
    bgroup = models.CharField(max_length=200,null=True,blank=False)
    gender = models.CharField(max_length=200,null=True,blank=False)
    img = models.ImageField(upload_to='image',null=True,blank=False)          