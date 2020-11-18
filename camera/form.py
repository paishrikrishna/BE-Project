from django import forms
from .models import events

class events_form(forms.ModelForm):
	class Meta:
		model = events
		fields={
			'organizer',
			'content',
			'date'
		}
