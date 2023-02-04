from django.shortcuts import render

# Create your views here.
def f_blog(request):
	return render(request,"v_blog.html")
