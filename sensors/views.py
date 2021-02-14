from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
from requested_events.models import req_events

from new_users.models import new_login_model

from .form import water_tank_form,lights_form,water_tank_date_form,lights_date_form
from .models import water_tank,lights,water_tank_date,lights_date
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

water_tank_switches = {
	"automation_switch":"false",
	"pump_switch":"false"
}
lights_status={
	"scheduled_lights":"false",
	"floor_no":"0",
	"floor_lights":"false",
	"scheduled_time_from":"",
	"scheduled_time_to":"",
	"all_lights":"false"	
	}

it_obj = list(lights.objects.all())
global lights_status
lights_status["scheduled_lights"] = it_obj[-1].scheduled_lights
lights_status["floor_no"] = it_obj[-1].floor_no
lights_status["floor_lights"] = it_obj[-1].floor_lights
lights_status["scheduled_time_from"]=it_obj[-1].scheduled_time_from
lights_status["scheduled_time_to"]=it_obj[-1].scheduled_time_to
lights_status["all_lights"]=it_obj[-1].all_lights

def sensors_index_page(request,user,auth):
	obj = list(req_events.objects.all())
	date_count = len(obj)

	obj = list(new_login_model.objects.all())
	date_count += len(obj)

	return render(request,"sensors.html",{"date_count":date_count,"user":user,"auth":auth})

def read_water_tank_status(request):
	obj = list(water_tank.objects.all())
	tank_status = {
	"water_level":obj[-1].level,
	"pump_status":obj[-1].pump_status,
	"automation_status":obj[-1].automation_status
	}
	print(date_time)
	return JsonResponse(tank_status)

def switch_status(request):
	global water_tank_switches
	water_tank_switches[request.GET['switch_name']]=request.GET['status']
	print(water_tank_switches)
	return JsonResponse(water_tank_switches)

	
def water_level(request):
	#print(water_tank_switches)
	now = datetime.datetime.utcnow()+datetime.timedelta(hours=5)+datetime.timedelta(minutes=30)
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	
	try:
		water_tank_form().save()
	except:
		obj = list(water_tank.objects.all())
		obj[-1].level = request.GET['water_level']
		obj[-1].pump_status = water_tank_switches['pump_switch']
		obj[-1].automation_status = water_tank_switches['automation_switch']
		obj[-1].save()

	try:
		water_tank_date_form().save()
	except:
		now = datetime.datetime.utcnow()+datetime.timedelta(hours=5)+datetime.timedelta(minutes=30)
		date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
		obj = list(water_tank_date.objects.all())
		obj[-1].date = date_time
		obj[-1].save()

	return JsonResponse(water_tank_switches)

def device_initial_setup(request):

	global water_tank_switches
	int_obj = list(water_tank.objects.all())
	water_tank_switches["automation_switch"]=int_obj[-1].automation_status
	water_tank_switches["pump_switch"]=int_obj[-1].pump_status

	it_obj = list(lights.objects.all())
	global lights_status
	lights_status["scheduled_lights"] = it_obj[-1].scheduled_lights
	lights_status["floor_no"] = it_obj[-1].floor_no
	lights_status["floor_lights"] = it_obj[-1].floor_lights
	lights_status["scheduled_time_from"]=it_obj[-1].scheduled_time_from
	lights_status["scheduled_time_to"]=it_obj[-1].scheduled_time_to
	lights_status["all_lights"]=it_obj[-1].all_lights
	return JsonResponse({"status":"sucess"})

def read_light_switch_status(request):
	obj = list(lights.objects.all())
	global lights_status
	lights_status["scheduled_lights"] = obj[-1].scheduled_lights
	lights_status["floor_no"] = obj[-1].floor_no
	lights_status["floor_lights"] = obj[-1].floor_lights
	lights_status["scheduled_time_from"]=obj[-1].scheduled_time_from
	lights_status["scheduled_time_to"]=obj[-1].scheduled_time_to
	lights_status["all_lights"]=obj[-1].all_lights
	return JsonResponse(lights_status)

def light_switch_status(request):
	global lights_status
	lights_status[request.GET['switch_name']]=request.GET['status']
	lights_status["scheduled_time_from"]=request.GET['from']
	lights_status["scheduled_time_to"]=request.GET['to']
	print(lights_status)
	return JsonResponse(lights_status)


def lights_operation(request):
	#print(water_tank_switches)

	try:
		lights_form().save()
	except:
		obj = list(lights.objects.all())
		obj[-1].scheduled_lights= lights_status["scheduled_lights"]
		obj[-1].floor_no= lights_status["floor_no"]
		obj[-1].floor_lights=lights_status["floor_lights"]
		obj[-1].scheduled_time_from=lights_status["scheduled_time_from"]
		obj[-1].scheduled_time_to=lights_status["scheduled_time_to"]
		obj[-1].all_lights=	lights_status["all_lights"]
		obj[-1].save()
	

	try:
		lights_date_form().save()
	except:
		now = datetime.datetime.utcnow()+datetime.timedelta(hours=5)+datetime.timedelta(minutes=30)
		date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
		obj = list(lights_date.objects.all())
		obj[-1].date = date_time
		obj[-1].save()

	return JsonResponse(lights_status)

def all_lights_operation(request):
	for i in range(0,6):
		try:
			lights_form().save()
		except:
			obj = list(lights.objects.all())
			obj[-1].scheduled_lights= lights_status["scheduled_lights"]
			obj[-1].floor_no= str(i)
			obj[-1].floor_lights=lights_status["all_lights"]
			obj[-1].scheduled_time_from=lights_status["scheduled_time_from"]
			obj[-1].scheduled_time_to=lights_status["scheduled_time_to"]
			obj[-1].all_lights=	lights_status["all_lights"]
			obj[-1].save()
		try:
			lights_date_form().save()
		except:
			now = datetime.datetime.utcnow()+datetime.timedelta(hours=5)+datetime.timedelta(minutes=30)
			date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
			obj = list(lights_date.objects.all())
			obj[-1].date = date_time
			obj[-1].save()

	obj = list(lights.objects.all())
	global lights_status
	lights_status["scheduled_lights"] = obj[-1].scheduled_lights
	lights_status["floor_no"] = obj[-1].floor_no
	lights_status["floor_lights"] = obj[-1].floor_lights
	lights_status["scheduled_time_from"]=obj[-1].scheduled_time_from
	lights_status["scheduled_time_to"]=obj[-1].scheduled_time_to
	lights_status["all_lights"]=obj[-1].all_lights

	return JsonResponse(lights_status)

def read_floor_light_status(request):
	obj = list(lights.objects.all())
	for i in range(1,len(obj)+1):
		if( str(obj[-i].floor_no) == str(request.GET['floor_number'])):
			print({"status":str(obj[-i].floor_lights)})
			return JsonResponse({"status":str(obj[-i].floor_lights)})	

def floor_and_light_status(request):
	global lights_status
	lights_status["floor_no"]= request.GET['floor_no']
	lights_status["floor_lights"]= request.GET['floor_lights']
	return JsonResponse({"status":"true"})

def date_and_time(request):
	now_time = datetime.datetime.utcnow()+datetime.timedelta(hours=5)+datetime.timedelta(minutes=30)
	time = now_time.strftime("%H:%M:%S")
	return JsonResponse({"time":time})

def lights_statu_s(request):
	lights_button = {}
	for i in range(0,6):
		obj = list(lights.objects.filter(floor_no=str(i)))
		lights_button[str(i)] = obj[-1].floor_lights
	return JsonResponse(lights_button)

def turn_hrd(request):
	global lights_status
	lights_status["all_lights"] = request.GET['status']
	for i in range(0,6):
		try:
			lights_form().save()
		except:
			obj = list(lights.objects.all())
			obj[-1].scheduled_lights= lights_status["scheduled_lights"]
			obj[-1].floor_no= str(i)
			obj[-1].floor_lights=lights_status["all_lights"]
			obj[-1].scheduled_time_from=lights_status["scheduled_time_from"]
			obj[-1].scheduled_time_to=lights_status["scheduled_time_to"]
			obj[-1].all_lights=	lights_status["all_lights"]
			obj[-1].save()

		try:
			lights_date_form().save()
		except:
			now = datetime.datetime.utcnow()+datetime.timedelta(hours=5)+datetime.timedelta(minutes=30)
			date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
			obj = list(lights_date.objects.all())
			obj[-1].date = date_time
			obj[-1].save()

	obj = list(lights.objects.all())
	global lights_status
	lights_status["scheduled_lights"] = obj[-1].scheduled_lights
	lights_status["floor_no"] = obj[-1].floor_no
	lights_status["floor_lights"] = obj[-1].floor_lights
	lights_status["scheduled_time_from"]=obj[-1].scheduled_time_from
	lights_status["scheduled_time_to"]=obj[-1].scheduled_time_to
	lights_status["all_lights"]=obj[-1].all_lights

	return JsonResponse(lights_status)

def export_data(request):

	if request.GET['name']=="water":
		# water level excel

		date,water_level,pump_status,automation_status = [],[],[],[]
		obj_tank = list(water_tank.objects.all())
		obj_tank_date = list(water_tank_date.objects.all())
		for i in range(1,len(obj_tank)+1):
			date.append(obj_tank_date[-i].date)
			water_level.append(obj_tank[-i].level)
			pump_status.append(obj_tank[-i].pump_status)
			automation_status.append(obj_tank[-i].automation_status)

		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename="Water Tank.xls"'

		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('Users')

		# Sheet header, first row

		columns = ['Date and time', 'Water Level', 'Pump Status', 'Automation Status',]


		rows = [date, water_level, pump_status, automation_status]

		font_style = xlwt.XFStyle()
		font_style.font.bold = True
		
		for j, col in enumerate(columns):
			ws.write(0, j, col,font_style)
		
		for cols , data in enumerate(rows):
			for row in range(1,len(data)+1):
				ws.write(row,cols,data[row-1],xlwt.XFStyle())

		wb.save(response)
		return response

	elif request.GET['name']=="lights":

		#lights excel 

		date,scheduled_lights,floor_no,floor_lights,scheduled_time_from,scheduled_time_to,all_lights = [],[],[],[],[],[],[]

		obj_tank = list(lights.objects.all())
		obj_tank_date = list(lights_date.objects.all())
		for i in range(1,len(obj_tank)+1):
			date.append(obj_tank_date[-1].date)
			scheduled_lights.append(obj_tank[-1].scheduled_lights)
			floor_no.append(obj_tank[-1].floor_no)
			floor_lights.append(obj_tank[-1].floor_lights)
			scheduled_time_from.append(obj_tank[-1].scheduled_time_from)
			scheduled_time_to.append(obj_tank[-1].scheduled_time_to)
			all_lights.append(obj_tank[-1].all_lights)

		response_lights = HttpResponse(content_type='application/ms-excel')
		response_lights['Content-Disposition'] = 'attachment; filename="Lights Status.xls"'

		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('Users')

		# Sheet header, first row


		font_style = xlwt.XFStyle()
		font_style.font.bold = True

		columns = ['Date and time', 'Scheduled Lights', 'Floor Number', 'Floor Lights','Scheduled From','Scheduled To','All Lights',]
		rows =[date, scheduled_lights, floor_no, floor_lights,scheduled_time_from,scheduled_time_to,all_lights]

		for j, col in enumerate(columns):
			ws.write(0, j, col,font_style)

		# Sheet body, remaining rows
		font_style = xlwt.XFStyle()

		for cols , data in enumerate(rows):
			for row in range(1,len(data)+1):
				ws.write(row,cols,data[row-1],xlwt.XFStyle())

		wb.save(response_lights)
		
		return response_lights


