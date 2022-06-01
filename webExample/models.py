from tabnanny import verbose
from django.db import models

class Users(models.Model):
    name = models.CharField('Ism', max_length=200)
    surname = models.CharField('Familiya', max_length=200)
    email = models.CharField('Elektron pochta', max_length=100, unique=True)
    pasword = models.CharField('Parol', max_length=100)

def  __str__(self):
    return self.name

class Meta :
    verbose_name = 'User'
    verbose_name_plural = 'Users'

    