from django import forms
from .models import Product

CHOICES = (
('large',"Large"),
("medium","Medium"),
('small',"Small")
	)


# class ProductForm (forms.Form):
# 	title= forms.CharField(label= "", widget= forms.TextInput(
# 		attrs={
# 		     "placeholder": "Title"
# 		}))
# 	description= forms.CharField(widget=forms.Textarea(
# 		attrs={
# 		        "placeholder" : "Description"

# 		}))
# 	price=forms.DecimalField()
# 	size = forms.ChoiceField(choices=CHOICES, required=False)


	# def clean_price(self):
	# 	price= self.cleaned_data.get("price")
	# 	if price <= 1:
	# 		raise forms.ValidationError ("Price Must be greater than Rs1")
	# 	else:
	# 		return price

	# def clean_title(self):
	# 	title= self.cleaned_data.get("title")
	# 	if len(title) > 15:
	# 		raise ValidationError ("Only Characters Allowed")
	# 	else:
	# 		return title

class ProductModelForm(forms.ModelForm):
	size = forms.ChoiceField(choices=CHOICES, required=False)

	class Meta:
		model= Product
		fields =[ 
		   "title",
		   "description",
		   "price",
		   "media",
		   
		]
		widgets ={
              "description" : forms.Textarea(
              	attrs={
              	 "placeholder": "Description"
              	}

              	)

		} 

	def clean_price(self):
		price= self.cleaned_data.get("price")
		if price <= 1:
			raise forms.ValidationError ("Price Must be greater than Rs1")
		else:
			return price

	def clean_title(self):
		title= self.cleaned_data.get("title")
		if len(title) > 15:
			raise ValidationError ("Only Characters Allowed")
		else:
			return title


			
			
			
