from django import forms
from .models import message_model

class message_form(forms.ModelForm):
	class Meta:
		model = message_model
		fields={
			'sender',
			'receiver',
			'message',
			'date',
		}
