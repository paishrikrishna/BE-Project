from django.db import models

# Create your models here.
class login_model(models.Model):
	username = models.TextField(default='n/a')
	password = models.TextField(default='N/A')
	auth = models.TextField(default='member')
	link = models.TextField(default='n/a')