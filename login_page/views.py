from django.shortcuts import render

# Create your views here.
from .models import login_model
from new_users.models import new_login_model
from .login_form import login_form
from requested_events.models import req_events

def login_index_page(request):
	if request.method == "POST":
		obj = list(req_events.objects.all())
		date_count = 0
		for i in obj:
			date_count += 1	
		obj = list(new_login_model.objects.all())
		for i in obj:
			date_count += 1	
		objects = login_model.objects.all()
		for i in objects:
			if (request.POST['email'] == i.username or request.POST['email'] == i.email) and request.POST['password'] == i.password:
				return render(request,"homepage.html",{"user":i.username,"auth":i.auth,"date_count":date_count,"email":i.email,"floor":i.floor,"flat":i.flat,"wing":i.wing,"link":i.link})
		return render(request,"login_page.html",{})
	else:		
		return render(request,"login_page.html",{})