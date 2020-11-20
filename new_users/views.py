from django.shortcuts import render
from .form import new_login_form
from .models import new_login_model
from login_page.login_form import login_form
from login_page.models import login_model
# Create your views here.
def new_user_index_page(request):
	if request.method == "POST":
		f=0
		obj = new_login_model.objects.all()
		for i in obj:
			if request.POST['username'] == i.username:
				f = 1
				break
		if f!=1:
			obj = login_model.objects.all()
			for i in obj:
				if request.POST['username'] == i.username:
					f = 2
					break
		if f==0:
			try:
				new_login_form().save()
			except:
				obj = new_login_model.objects.get(username='n/a')
				obj.username = request.POST['username']
				obj.password = request.POST['password']
				obj.save()
		return render(request,"new_user.html",{"flag":str(f)})
	else:

		return render(request,"new_user.html",{"flag":"3"})
				

		