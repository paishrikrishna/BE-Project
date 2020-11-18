from django.shortcuts import render

# Create your views here.
def cal_index_page(request):
	if request.method == 'GET':
		return render(request,"calander.html",{"month":10,"year":2020})
	else:
		if request.POST["action"] == "Next" :
			if int(request.POST['month']) == 12: 
				return render(request,"calander.html",{"month":1,"year":int(request.POST['year'])+1})
			elif int(request.POST['month']) < 12:
				return render(request,"calander.html",{"month":int(request.POST['month'])+1,"year":int(request.POST['year'])})
		else:
			if int(request.POST['month']) == 1: 
				return render(request,"calander.html",{"month":12,"year":int(request.POST['year'])-1})
			elif int(request.POST['month']) > 1:
				return render(request,"calander.html",{"month":int(request.POST['month'])-1,"year":int(request.POST['year'])})