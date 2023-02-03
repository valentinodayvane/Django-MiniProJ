from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,"home.html")

def contact(request):
	gens = ["randria","rakoto","rabe","jo","alain"]
	context = {"noms":gens}
	return render(request,"contact.html",context)