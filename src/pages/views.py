from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>") # string of HTML code
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context ={
	"my_text": "This is about Mukto learning Django",
	"my_number": 123,
	"my_list": ["item1", "item2", "item3"],
	"my_html": "<h1>HTML tag</h1>"
	}
	return render(request, "about.html", my_context)
