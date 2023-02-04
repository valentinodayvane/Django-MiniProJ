from django.shortcuts import render
from django.http import HttpResponse

def f_home(request):
	"""
	"""
	return render(request,"v_home.html")

def f_ami(request):
	gens = ["rakoto","rabe","joe", "jack","will"]
	context = {"amis":gens}
	return render(request,"v_ami.html",context)
	