from django.db import models

# Create your models here.
class water_tank(models.Model):

	level = models.TextField(default='40')
	pump_status = models.TextField(default='false')
	automation_status = models.TextField(default='false')
	
class lights(models.Model):
	scheduled_lights = models.TextField(default='false')
	floor_no = models.TextField(default='0')
	floor_lights = models.TextField(default='false')
	scheduled_time_from = models.TextField(default='00:00')
	scheduled_time_to = models.TextField(default='00:00')
	all_lights = models.TextField(default='false')
	
class water_tank_date(models.Model):
	date = models.TextField(default='n/a')

class lights_date(models.Model):
	date = models.TextField(default='n/a')