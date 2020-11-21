from django.db import models

# Create your models here.
class message_model(models.Model):
	sender = models.TextField(default='n/a')
	receiver = models.TextField(default='N/A')
	message = models.TextField(default='N/A')
	date = models.TextField(default='N/A')