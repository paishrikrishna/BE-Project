from django.shortcuts import render
import datetime

# Create your views here.
x = str(datetime.datetime.now()).split("-")

def cal_index_page(request):
	if request.method == 'GET':
		return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":x[1],"year":int(x[0])})
	else:
		print(request.POST)
		if request.POST["action"] == "Next" :
			if int(request.POST['month']) == 12: 
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":1,"year":int(request.POST['year'])+1})
			elif int(request.POST['month']) < 12:
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month'])+1,"year":int(request.POST['year'])})
		else:
			if int(request.POST['month']) == 1: 
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":12,"year":int(request.POST['year'])-1})
			elif int(request.POST['month']) > 1:
				return render(request,"calander.html",{"date":x[2].split(" ")[0],"month":int(request.POST['month'])-1,"year":int(request.POST['year'])})