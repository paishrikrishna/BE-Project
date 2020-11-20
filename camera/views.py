from django.shortcuts import render

# Create your views here.
from requested_events.form import req_events_form
from requested_events.models import req_events

from new_users.models import new_login_model

def cam_index_page(request,user):
	obj = list(req_events.objects.all())
	date_count = 0
	for i in obj:
		date_count += 1
	obj = list(new_login_model.objects.all())
	for i in obj:
		date_count += 1	
	return render(request,"camera.html",{"date_count":date_count,"user":user})

