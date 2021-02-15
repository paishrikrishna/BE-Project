from django.db import models

# Create your models here.
class entry_exit_model(models.Model):
	username = models.TextField(default='n/a')
	auth = models.TextField(default='member')
	wing = models.TextField(default='n/a')
	floor = models.TextField(default='n/a')
	number = models.TextField(default='n/a')
	date = models.TextField(default='n/a')
	