from django.shortcuts import render

# Create your views here.
from requested_events.form import req_events_form
from requested_events.models import req_events

from new_users.models import new_login_model

def cam_index_page(request,user,auth):
	obj = list(req_events.objects.all())
	date_count = len(obj)

	obj = list(new_login_model.objects.all())
	date_count += len(obj)
	return render(request,"camera.html",{"date_count":date_count,"user":user,"auth":auth})

