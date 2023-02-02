from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, "homepage.html")
def contact(request):
	gens = ["rakoto","randi","neo","keanu"]
	context = {"noms": gens}
	return render(request, "contactpage.html", context)


