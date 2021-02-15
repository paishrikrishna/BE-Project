from django.shortcuts import render

# Create your views here.

from requested_events.models import req_events

from new_users.models import new_login_model
from login_page.models import login_model

def home_index_page(request,user,auth):
	obj = list(req_events.objects.all())
	date_count = len(obj)

	obj = list(new_login_model.objects.all())
	date_count += len(obj)
	i = login_model.objects.get(username=user)
	return render(request,"homepage.html",{"user":i.username,"auth":i.auth,"date_count":date_count,"email":i.email,"floor":i.floor,"flat":i.flat,"wing":i.wing,"link":i.link})