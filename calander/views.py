from django.shortcuts import render

# Create your views here.
def cal_index_page(request):
	return render(request,"calander.html")