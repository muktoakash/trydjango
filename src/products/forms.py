from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label='', 
		widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	description = forms.CharField(required=False,
		widget=forms.Textarea(
			attrs={
	 			"class": "new-class-name two",
	 			"id": "my-id-for-textarea",
	 			"rows": 10,
	 			"cols": 120,
	 			"placeholder": "Your description",
	 	}))
	price = forms.DecimalField(initial = 199.99)
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
			]
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "trydjango" in title:
			raise forms.ValidationError("This is not a valid title")
		return title

class RawProductForm(forms.Form):
	title = forms.CharField(label='', 
		widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	description = forms.CharField(required=False,
		widget=forms.Textarea(
			attrs={
	 			"class": "new-class-name two",
	 			"id": "my-id-for-textarea",
	 			"rows": 10,
	 			"cols": 120,
	 			"placeholder": "Your description",
	 	}))
	price = forms.DecimalField(initial = 199.99)