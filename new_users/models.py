from django.db import models

# Create your models here.
class new_login_model(models.Model):
	username = models.TextField(default='n/a')
	password = models.TextField(default='N/A')
	