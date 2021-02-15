from django import forms
from .models import new_login_model

class new_login_form(forms.ModelForm):
	class Meta:
		model = new_login_model
		fields={
			'username',
			'password',
			'link',
			'email',
			'wing',
			'floor',
			'flat',
		}
