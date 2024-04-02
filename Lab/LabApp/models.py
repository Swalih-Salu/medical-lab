from django.db import models

# Create your models here.
class bkapmt(models.Model):
    name=models.TextField()
    number=models.IntegerField()
    city=models.TextField()

class TeleRadio(models.Model):
    name=models.TextField()
    email=models.EmailField()
    number=models.IntegerField()
    designation=models.TextField()
    city=models.TextField()
    
class Category(models.Model):
    name=models.TextField()
    desc=models.TextField()
    sub=models.TextField()
    
class bkapmtHaemolgy(models.Model):
    name=models.TextField()
    number=models.IntegerField()
    city=models.TextField()
    
class bkapmtBiochem(models.Model):
    name=models.TextField()
    number=models.IntegerField()
    city=models.TextField()
    
class bkapmtImmuno(models.Model):
    name=models.TextField()
    number=models.IntegerField()
    city=models.TextField()
    
