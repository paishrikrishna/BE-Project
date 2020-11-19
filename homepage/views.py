from django.shortcuts import render

# Create your views here.

def home_index_page(request,user):
	return render(request,"homepage.html",{"user":user})