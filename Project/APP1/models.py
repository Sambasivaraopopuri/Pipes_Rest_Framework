from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Pipes(models.Model):
    Tilte=models.CharField(max_length=200)
    Desc=models.CharField(max_length=1000)
    Size=models.CharField(max_length=5)
    Posted_By=models.CharField(max_length=150)
    Qulity=models.CharField(max_length=25)
    Grade=models.CharField(max_length=25)
    Color=models.CharField(max_length=20)
    image=models.CharField(max_length=2000)
    
    class Meta:
        db_table="Pipes"