from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from requested_events.models import req_events

from new_users.models import new_login_model

from .form import water_tank_form,lights_form
from .models import water_tank,lights
import datetime

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
	
	return JsonResponse(tank_status)

def switch_status(request):
	global water_tank_switches
	water_tank_switches[request.GET['switch_name']]=request.GET['status']
	print(water_tank_switches)
	return JsonResponse(water_tank_switches)

	
def water_level(request):
	#print(water_tank_switches)

	try:
		water_tank_form().save()
	except:
		obj = list(water_tank.objects.all())
		obj[-1].level = request.GET['water_level']
		obj[-1].pump_status = water_tank_switches['pump_switch']
		obj[-1].automation_status = water_tank_switches['automation_switch']
		obj[-1].save()

	return JsonResponse(water_tank_switches)

def device_initial_setup(request):

	global water_tank_switches
	int_obj = list(water_tank.objects.all())
	water_tank_switches["automation_switch"]=int_obj[-1].automation_status
	water_tank_switches["pump_switch"]=int_obj[-1].pump_status

	obj = list(lights.objects.all())
	global lights_status
	lights_status["scheduled_lights"] = obj[-1].scheduled_lights
	lights_status["floor_no"] = obj[-1].floor_no
	lights_status["floor_lights"] = obj[-1].floor_lights
	lights_status["scheduled_time_from"]=obj[-1].scheduled_time_from
	lights_status["scheduled_time_to"]=obj[-1].scheduled_time_to
	lights_status["all_lights"]=obj[-1].all_lights

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