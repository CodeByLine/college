from django.db import models
from django.urls import reverse 
from datetime import date
# from django.contrib.auth.models import User
# import uuid # Required for unique book instances 



class School(models.Model):
    name = models.CharField(max_length=200)
    school_description = models.TextField(max_length=1000)
  
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school-detail', args=[str(self.id)])




