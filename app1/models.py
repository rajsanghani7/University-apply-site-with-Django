import email
from random import choice
from unicodedata import name
from django.db import models
from django.forms import CharField
from numpy import number

# Feedback Model
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    desc = models.TextField("")
    def __str__(self):
        return self.email
    
# Form Model
class Form(models.Model):
    choice = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    university = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=4)
    ielts = models.CharField(max_length=4)

    def __str__(self):
        return self.name + ' , ' + self.choice


# Pennsylvania model
# class Pennsylvania(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     number = models.CharField(max_length=10)
#     university = models.CharField(max_length=100)
#     cgpa = models.CharField(max_length=4)
#     ielts = models.CharField(max_length=4)