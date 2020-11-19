from django.shortcuts import render

from .form import events_form
from .models import events
# Create your views here.
import datetime

x = str(datetime.datetime.now()).split("-")

def cal_index_page(request):
	obj = list(events.objects.all())
	organizer , content , date = [],[],[]
	for i in obj:
		organizer.append(i.organizer)
		content.append(i.content)
		date.append(i.date)
	print(date)
	if request.method == 'GET':
		return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":x[1],"year":int(x[0]),"organizer":organizer,"event_dates":date,"content":content})
	else:
		print(request.POST)
		if request.POST["action"]=="Add Event":
			try:
				events_form().save()
			except:
				obj = events.objects.get(organizer='n/a')
				obj.organizer = request.POST['Organizer']
				obj.content = request.POST['Agenda']
				obj.date = request.POST['New_date']
				obj.save()
				
			obj = list(events.objects.all())
			organizer , content , date = [],[],[]
			for i in obj:
				organizer.append(i.organizer)
				content.append(i.content)
				date.append(i.date)
			return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month']),"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content})
		elif request.POST["action"] == "Next" :
			if int(request.POST['month']) == 12: 
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":1,"year":int(request.POST['year'])+1,"organizer":organizer,"event_dates":date,"content":content})
			elif int(request.POST['month']) < 12:
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month'])+1,"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content})
		else:
			if int(request.POST['month']) == 1: 
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":12,"year":int(request.POST['year'])-1,"organizer":organizer,"event_dates":date,"content":content})
			elif int(request.POST['month']) > 1:
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month'])-1,"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content})