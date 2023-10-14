from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, RawProductFrom

# Create your views here.

def product_create_view(request):
	# if request.method == 'POST':
	# 	my_new_title = request.POST.get('title')
	# 	Product.objects.create(title=my_new_title)
	
	# my_form = RawProductFrom()
	# if request.method == "POST":
	# 	my_form = RawProductFrom(request.POST)
	# 	if my_form.is_valid():
	# 		# now the data is good
	# 		print(my_form.cleaned_data)
	# 		Product.objects.create(**my_form.cleaned_data)
	# 	else:
	# 		print(my_form.errors)
	# context={"form": my_form }
	# return render(request, "products/product_create.html", context)
	
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
	'form': form
	}
	return render(request, "products/product_create.html", context)

def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context={
	# 	'title': obj.title,
	# 	'description': obj.description
	# }
	context = {
	'object' : obj
	}
	return render(request, "products/detail.html", context)
