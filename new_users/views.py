from django.shortcuts import render

# Create your views here.
def new_user_index_page(request):
	return render(request,"new_user.html",{})