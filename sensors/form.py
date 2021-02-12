from django import forms
from .models import water_tank,lights

class water_tank_form(forms.ModelForm):
	class Meta:
		model = water_tank
		fields={
			'level',
			'pump_status',
			'automation_status'
		}

class lights_form(forms.ModelForm):
	class Meta:
		model = lights
		fields={
			'scheduled_lights',
			'floor_no',
			'floor_lights',
			'scheduled_time_from',
			'scheduled_time_to',
			'all_lights'
		}

