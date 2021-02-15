from django.shortcuts import render
from django.http import HttpResponse
import qrcode

# Create your views here.

from requested_events.models import req_events

from new_users.models import new_login_model
from login_page.models import login_model

def home_index_page(request,user,auth):
	obj = list(req_events.objects.all())
	date_count = len(obj)

	obj = list(new_login_model.objects.all())
	date_count += len(obj)
	i = login_model.objects.get(username=user)
	return render(request,"homepage.html",{"user":i.username,"auth":i.auth,"date_count":date_count,"email":i.email,"floor":i.floor,"flat":i.flat,"wing":i.wing,"link":i.link})

def qr_code(request,user):
	input_data = str(user)
	qr = qrcode.QRCode(
	        version=1,
	        box_size=10,
	        border=5)
	qr.add_data(input_data)
	qr.make(fit=True)
	img = qr.make_image(fill='black', back_color='white')
	img.save('qrcode_'+str(user)+'_.png')
	return HttpResponse(open('qrcode_'+str(user)+'_.png', "rb").read(), content_type="image/png")