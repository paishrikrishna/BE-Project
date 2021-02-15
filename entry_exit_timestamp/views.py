from requested_events.models import req_events
from django.shortcuts import render
from new_users.models import new_login_model
from login_page.models import login_model
from django.http import HttpResponse

from .entry_exit_form import entry_exit_form
from .models import entry_exit_model

import datetime
import xlwt
import datetime
import pandas as pd

now = datetime.datetime.utcnow()+datetime.timedelta(hours=5)+datetime.timedelta(minutes=30) # current date and time

year = now.strftime("%Y")

month = now.strftime("%m")

day = now.strftime("%d")

time = now.strftime("%H:%M:%S")

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")



def timestamp_index_page(request,user,auth):

	if request.method == "POST":
		now = datetime.datetime.utcnow()+datetime.timedelta(hours=5)+datetime.timedelta(minutes=30)
		date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
		try:
			entry_exit_form().save()
		except:
			objs = list(entry_exit_model.objects.all())
			objs[-1].username = request.POST['name']
			objs[-1].auth = request.POST['reason']
			objs[-1].wing = request.POST['wing']
			objs[-1].floor = request.POST['floor']
			objs[-1].number = request.POST['contact']
			objs[-1].date = date_time
			objs[-1].save()		


	obj = list(req_events.objects.all())
	date_count = len(obj)

	obj = list(new_login_model.objects.all())
	date_count += len(obj)
	i = login_model.objects.get(username=user)
	return render(request,"timestamp.html",{"user":i.username,"auth":i.auth,"date_count":date_count,"email":i.email,"floor":i.floor,"flat":i.flat,"wing":i.wing,"link":i.link})

def export_timestamps(request):

	date,username,auth,wing,floor,number=[],[],[],[],[],[]
	
	obj_tank = list(entry_exit_model.objects.all())
	for i in range(1,len(obj_tank)+1):
		username.append(obj_tank[-i].username)
		auth.append(obj_tank[-i].auth)
		wing.append(obj_tank[-i].wing)
		floor.append(obj_tank[-i].floor)
		number.append(obj_tank[-i].number)
		date.append(obj_tank[-i].date)
		
	response_lights = HttpResponse(content_type='application/ms-excel')
	response_lights['Content-Disposition'] = 'attachment; filename="Entry Exit Status.xls"'

	wb = xlwt.Workbook(encoding='utf-8')
	ws = wb.add_sheet('Users')

	# Sheet header, first row


	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['Date and Time','Name', 'Reason to visit', 'wing', 'Floor and Flat number','Contact Number',]
	rows =[date,username,auth,wing,floor,number]

	for j, col in enumerate(columns):
		ws.write(0, j, col,font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	for cols , data in enumerate(rows):
		for row in range(1,len(data)+1):
			ws.write(row,cols,data[row-1],xlwt.XFStyle())

	wb.save(response_lights)
	
	return response_lights