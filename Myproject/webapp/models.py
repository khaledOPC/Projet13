from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)



class Activity(models.Model):
	name = models.CharField(max_length=100)
	lieu = models.CharField(max_length=200)
	date = models.DateField()
	upload = models.ImageField(upload_to ='uploads/') 
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Reservation(models.Model):
	lieu = models.CharField(max_length=200)
	date = models.DateField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE)