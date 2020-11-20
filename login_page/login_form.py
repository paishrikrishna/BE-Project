from django import forms
from .models import login_model

class login_form(forms.ModelForm):
	class Meta:
		model = login_model
		fields={
			'username',
			'password',
			'auth',
		}
