from django.shortcuts import render

# Create your views here.

def home_index_page(request):
	return render(request,"homepage.html")