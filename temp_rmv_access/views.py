from django.shortcuts import render
from django.http import HttpResponse
import qrcode

# Create your views here.
from requested_events.models import req_events
from login_page.models import login_model

def temp_rmv_access(request,user,auth):
	if request.method == "POST":
		if request.POST['action']=="Delete User":
			obj = login_model.objects.get(email=(request.POST['email']))
			obj.delete()

	obj = list(req_events.objects.all())
	organizer , content , date ,ID= [],[],[],[]
	for i in obj:
		organizer.append(i.organizer)
		content.append(i.content)
		date.append(i.date)
		ID.append(i.id)	

	obj = list(login_model.objects.all())
	username,password ,user_ID,floor,wing,link,pswd,ID= [],[],[],[],[],[],[],[]
	for i in obj:
		username.append(i.username)
		password.append(i.email)
		user_ID.append(i.flat)
		ID.append(i.id)
		floor.append(i.floor)
		wing.append(i.wing)
		link.append(i.link)
		pswd.append(i.password)
	

	return render(request,"temp_rmv_access.html",{"ID":ID,"floor":floor,"pswd":pswd,"wing":wing,"link":link,"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"username":username,"password":password,"user_ID":user_ID,"auth":auth})

