from django.db import models

# Create your models here.
from django.dispatch import receiver
from elasticsearch_dsl import Index


class Student(models.Model):
    studentname = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()



