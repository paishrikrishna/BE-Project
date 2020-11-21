from django import forms
from .models import notice_model

class notice_form(forms.ModelForm):
	class Meta:
		model = notice_model
		fields={
			'date',
			'subject',
			'issuer',
			'content',
		}
