from django.shortcuts import render

from calander.form import events_form
from calander.models import events

from .form import req_events_form
from .models import req_events
# Create your views here.

def req_events_index_page(request,user):
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

	obj = list(req_events.objects.all())
	organizer , content , date ,ID= [],[],[],[]
	for i in obj:
		organizer.append(i.organizer)
		content.append(i.content)
		date.append(i.date)
		ID.append(i.id)	
	return render(request,"requested_events.html",{"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user})