from django.db import models

# Create your models here.
class water_tank(models.Model):
	level = models.TextField(default='n/a')
	pump_status = models.TextField(default='N/A')
	automation_status = models.TextField(default='N/A')
	
class lights(models.Model):
	scheduled_lights = models.TextField(default='n/a')
	floor_no = models.TextField(default='N/A')
	floor_lights = models.TextField(default='N/A')
	scheduled_time_from = models.TextField(default='n/a')
	scheduled_time_to = models.TextField(default='n/a')
	all_lights = models.TextField(default='N/A')
	