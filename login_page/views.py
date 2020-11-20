from django.shortcuts import render

# Create your views here.
from .login_form import login_form
from .models import login_model

def login_index_page(request):
	if request.method == "POST":
		objects = login_model.objects.all()
		for i in objects:
			if request.POST['email'] == i.username and request.POST['password'] == i.password:
				return render(request,"homepage.html",{"user":i.auth})
	else:		
		return render(request,"login_page.html",{})