from django.shortcuts import render

# Create your views here.

def cam_index_page(request):
	return render(request,"camera.html")

