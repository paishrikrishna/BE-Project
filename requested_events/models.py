from django.db import models

# Create your models here.
class req_events(models.Model):
	organizer = models.TextField(default='n/a')
	content = models.TextField(default='N/A')
	date = models.TextField(default='N/A')
	