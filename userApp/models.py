from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    user= models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    picture=models.ImageField(max_length=225,upload_to='pic/',default=3)
    def __str__(self):
        return self.name
        