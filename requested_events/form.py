from django import forms
from .models import req_events

class req_events_form(forms.ModelForm):
	class Meta:
		model = req_events
		fields={
			'organizer',
			'content',
			'date'
		}
