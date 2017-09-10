# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=50)
    passward=models.CharField(max_length=50)


    def __str__(self):
         return (self.username)

class blogs(models.Model):

    log_in=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    para=models.CharField(max_length=100000,null=True)
    title=models.CharField(max_length=250)


    def __str__(self):
        return (self.title)
