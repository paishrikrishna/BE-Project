from django.shortcuts import render

from .form import events_form
from .models import events

from requested_events.form import req_events_form
from requested_events.models import req_events

from new_users.models import new_login_model
# Create your views here.
import datetime

x = str(datetime.datetime.now()).split("-")

def cal_index_page(request,user,auth):
	obj = list(req_events.objects.all())
	date_count = 0
	for i in obj:
		date_count += 1	
	obj = list(new_login_model.objects.all())
	for i in obj:
		date_count += 1	

	request.session.flush()
	obj = list(events.objects.all())
	organizer , content , date ,ID= [],[],[],[]
	for i in obj:
		organizer.append(i.organizer)
		content.append(i.content)
		date.append(i.date)
		ID.append(i.id)
	print(date)
	if request.method == 'GET':
		return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":x[1],"year":int(x[0]),"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})
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
			organizer , content , date ,ID = [],[],[],[]
			for i in obj:
				organizer.append(i.organizer)
				content.append(i.content)
				date.append(i.date)
				ID.append(i.id)
			return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month']),"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})
		
		elif request.POST["action"]=="Edit Event":
			
			if(list(request.POST['old_Agenda'])[0]==" "):
				content = "".join(list(request.POST['old_Agenda'])[1:])
				organizer = "".join(list(request.POST['old_Organizer'])[1:])
			else:
				content = request.POST['old_Agenda']
				organizer = request.POST['old_Organizer']
			
			obj = events.objects.get(content=content,date=request.POST['old_New_date'],organizer=organizer)
			obj.organizer = request.POST['edit_Organizer']
			obj.content = request.POST['edit_Agenda']
			obj.date = request.POST['edit_New_date']
			obj.save()
				
			obj = list(events.objects.all())
			organizer , content , date ,ID= [],[],[],[]
			for i in obj:
				organizer.append(i.organizer)
				content.append(i.content)
				date.append(i.date)
				ID.append(i.id)

			return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month']),"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})
		
		elif request.POST["action"]=="Delete Event":
			
			if(list(request.POST['old_Agenda'])[0]==" "):
				content = "".join(list(request.POST['old_Agenda'])[1:])
				organizer = "".join(list(request.POST['old_Organizer'])[1:])
			else:
				content = request.POST['old_Agenda']
				organizer = request.POST['old_Organizer']
			
			obj = events.objects.get(content=content,date=request.POST['old_New_date'],organizer=organizer)
			obj.delete()
				
			obj = list(events.objects.all())
			organizer , content , date ,ID= [],[],[],[]
			for i in obj:
				organizer.append(i.organizer)
				content.append(i.content)
				date.append(i.date)
				ID.append(i.id)

			return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month']),"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})
		elif request.POST["action"]=="Request Event":
			
			if(list(request.POST['req_Agenda'])[0]==" "):
				content = "".join(list(request.POST['req_Agenda'])[1:])
				organizer = "".join(list(request.POST['req_Organizer'])[1:])
			else:
				content = request.POST['req_Agenda']
				organizer = request.POST['req_Organizer']
			
			try:
				req_events_form().save()
			except:
				obj = req_events.objects.get(organizer='n/a')
				obj.organizer = request.POST['req_Organizer']
				obj.content = request.POST['req_Agenda']
				obj.date = request.POST['req_New_date']
				obj.save()
				
			obj = list(events.objects.all())
			organizer , content , date ,ID = [],[],[],[]
			for i in obj:
				organizer.append(i.organizer)
				content.append(i.content)
				date.append(i.date)
				ID.append(i.id)
			return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month']),"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})
		
		elif request.POST["action"] == "Next" :
			if int(request.POST['month']) == 12: 
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":1,"year":int(request.POST['year'])+1,"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})
			elif int(request.POST['month']) < 12:
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month'])+1,"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})
		else:
			if int(request.POST['month']) == 1: 
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":12,"year":int(request.POST['year'])-1,"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})
			elif int(request.POST['month']) > 1:
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month'])-1,"year":int(request.POST['year']),"organizer":organizer,"event_dates":date,"content":content,"ID":ID,"user":user,"auth":auth,"date_count":date_count})