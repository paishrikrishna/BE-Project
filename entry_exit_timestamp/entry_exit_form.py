from django import forms
from .models import entry_exit_model

class entry_exit_form(forms.ModelForm):
	class Meta:
		model = entry_exit_model
		fields={
			'username',
			'auth',
			'wing',
			'floor',
			'number',
			'date',
			
		}