from django.db import models

# Create your models here.
class notice_model(models.Model):
	date = models.TextField(default='n/a')
	subject = models.TextField(default='N/A')
	issuer = models.TextField(default='N/A')
	content = models.TextField(default='N/A')
	