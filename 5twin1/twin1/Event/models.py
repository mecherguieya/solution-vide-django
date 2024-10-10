from django.db import models

# Create your models here.

#Héritage ena 
class Event(models.Model):
    
    title=models.CharField(max_length=10)
    