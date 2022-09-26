from django.db import models
from django.forms import IntegerField

# Create your models here.
class addStd(models.Model):
    stdID=models.IntegerField(primary_key=True)
    stdName=models.CharField(max_length=25)
    stdFather=models.CharField(max_length=20)
    stdDOB=models.CharField(max_length=25)
    stdGender=models.CharField(max_length=25,null=True, blank=True)
    stdCNIC=models.CharField(max_length=20,null=True, blank=True)
    stdAddress=models.CharField(max_length=100,null=True, blank=True)    
    stdMobile=models.CharField(max_length=25,null=True, blank=True)
    stdEmail=models.EmailField(max_length=30,null=True, blank=True)
    stdEmergencyContactPerson=models.CharField(max_length=25,null=True, blank=True)
    stdEmergencyContactPersonNumber=models.CharField(max_length=25,null=True, blank=True)
    stdPhoto=models.CharField(max_length=25,null=True, blank=True)
    stdCourse=models.CharField(max_length=20,null=True, blank=True)
    def __str__(self):
        return str(self.stdName)
