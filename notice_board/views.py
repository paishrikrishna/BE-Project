from django.shortcuts import render

# Create your views here.

from requested_events.models import req_events

from new_users.models import new_login_model

from .form import notice_form
from .models import notice_model

def notice_index_page(request,user,auth):
	obj = list(req_events.objects.all())
	date_count = len(obj)

	obj = list(new_login_model.objects.all())
	date_count += len(obj)

	if request.method=='POST':
		if request.POST['action']=='Publish Notice':
			try:
				notice_form().save()
			except:
				obj = notice_model.objects.get(date='n/a')
				obj.date = request.POST['date']
				obj.issuer = request.POST['issued_by']
				obj.subject = request.POST['Subject']
				obj.content = request.POST['content']
				obj.save()
		elif request.POST['action']=='Done Editing':
			obj = notice_model.objects.get(id=int(request.POST['user_row']))
			obj.date = request.POST['published on']
			obj.issuer = request.POST['issuer']
			obj.subject = request.POST['subject']
			obj.content = request.POST['matter']
			obj.save()
		elif request.POST['action']=='Delete Notice':
			obj = notice_model.objects.get(id=int(request.POST['user_row']))
			obj.delete()
			
	date , issuer , subject , content , ID = [],[],[],[],[]
	obj = notice_model.objects.all()
	notice_count = len(obj)
	for i in obj:
		date.append(i.date)
		issuer.append(i.issuer)
		subject.append(i.subject)
		content.append(i.content)
		ID.append(i.id)

	return render(request,"notice_board.html",{"notice_count":notice_count,"date_count":date_count,"user":user,"auth":auth,"date":date,"issuer":issuer,"subject":subject,"content":content,"ID":ID})
