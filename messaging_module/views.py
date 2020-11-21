from django.shortcuts import render

# Create your views here.
from requested_events.form import req_events_form
from requested_events.models import req_events

from new_users.models import new_login_model
from .msg_form import message_form
from .models import message_model
from login_page.models import login_model

import datetime

x = str(datetime.datetime.now()).split("-")

def message_index_page(request,user,auth):
	username=[]
	messages=[]
	date = []
	obj = list(req_events.objects.all())
	date_count = len(obj)

	obj = list(new_login_model.objects.all())
	date_count += len(obj)


	if(request.method=="POST"):
		if request.POST['action']=="Send Message":
			try:
				message_form().save()
			except:
				obj = message_model.objects.get(sender='n/a')
				obj.sender = request.POST['sender']
				obj.receiver = request.POST['receiver']
				obj.message = request.POST['message']
				obj.date = x[0]+"-"+x[1]+"-"+x[2].split(" ")[0]
				obj.save()


	obj = list(message_model.objects.all())
	for i in obj:
		if i.receiver == user:
			username.append(i.sender)
			messages.append(i.message)
			date.append(i.date)
		
	all_users=[]
	obj = list(login_model.objects.all())
	for i in obj:
		all_users.append(i.username)

	return render(request,"message.html",{"date_count":date_count,"user":user,"auth":auth,"username":username,"messages":messages,"all_users":all_users,"date":date})

