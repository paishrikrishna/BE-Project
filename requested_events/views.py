from django.shortcuts import render

from calander.form import events_form
from calander.models import events

from .form import req_events_form
from .models import req_events

from login_page.login_form import login_form
from login_page.models import login_model
from new_users.models import new_login_model


# Create your views here.

def req_events_index_page(request,user,auth):
	if request.method=="POST":
		if request.POST['action']=="Add Event":
			try:
				events_form().save()
			except:
				obj = events.objects.get(organizer='n/a')
				obj.organizer = request.POST['Organizer']
				obj.content = request.POST['Agenda']
				obj.date = request.POST['New_date']
				obj.save()

			obj = req_events.objects.get(id=int(request.POST['row']))
			obj.delete()
		elif request.POST['action']=="Delete Event":
			obj = req_events.objects.get(id=int(request.POST['row']))
			obj.delete()
		elif request.POST['action']=="Add User":
			try:
				login_form().save()
			except:
				obj = login_model.objects.get(username='n/a')
				obj.username = request.POST['username']
				obj.password = request.POST['password']
				obj.auth = "member"
				obj.link = request.POST['link']
				obj.email = request.POST['email']
				obj.wing = request.POST['wing']
				obj.floor = request.POST['floor']
				obj.flat = request.POST['flat']
				obj.save()

			obj = new_login_model.objects.get(email=(request.POST['email']))
			obj.delete()
		elif request.POST['action']=="Delete User":
			obj = new_login_model.objects.get(email=(request.POST['email']))
			obj.delete()

	obj = list(req_events.objects.all())
	organizer , content , date ,ID= [],[],[],[]
	for i in obj:
		organizer.append(i.organizer)
		content.append(i.content)
		date.append(i.date)
		ID.append(i.id)	

	obj = list(new_login_model.objects.all())
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

	return render(request,"requested_events.html",{"ID":ID,"floor":floor,"pswd":pswd,"wing":wing,"link":link,"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"username":username,"password":password,"user_ID":user_ID,"auth":auth})