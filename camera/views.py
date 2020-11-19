from django.shortcuts import render

# Create your views here.

def cam_index_page(request,user):
	return render(request,"camera.html",{"user":user})

