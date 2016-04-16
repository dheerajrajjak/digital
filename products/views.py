from django.shortcuts import render, get_object_or_404
import os
from django.db.models import Q
from django.core.servers.basehttp import FileWrapper
from mimetypes import guess_type
from django.core.files import File
from django.conf import settings
from .models import Product
from django.http import Http404, HttpResponse
from .forms import ProductModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from .mixins import SubmitMixin,StaffRequiredMixin, ProductManagerMixin


# Create your views here.




class ProductCreateView(StaffRequiredMixin,SubmitMixin,CreateView):
	model=Product
	template_name= "form.html"
	form_class= ProductModelForm
	# success_url='/product/create/'
	submit_btn = "Create Product"

	def form_valid(self,form):
		user= self.request.user
		form.instance.user=user
		valid_data =super(ProductCreateView,self).form_valid(form)
		form.instance.group.add(user)
		return valid_data


	
class ProductUpdateView(ProductManagerMixin, SubmitMixin,UpdateView):
	model=Product
	template_name= "form.html"
	form_class= ProductModelForm
	# success_url='/product-list/'
	submit_btn= "Update Product"


	
class ProductDetailView(DetailView):
	model=Product


class ProductDownloadView(DetailView):
	model=Product

	def get(self,request,*args,**kwargs):
		obj=self.get_object()
		filepath= os.path.join(settings.PROTECTED_ROOT, obj.media.name)
		# f=open(filepath, 'r')
		# File(f).closed
		wrapper= FileWrapper(file(filepath))
		mimetype = 'applictaion/force-download'
		guessed_type= guess_type(filepath)[0]
		if guessed_type:
			mimetype=guessed_type
		response= HttpResponse(wrapper, content_type= mimetype)
		if not request.GET.get("preview"):
			response["Content-Disposition"]="attachment; filename=%s" %(obj.media.name)
		response['X-Sendfile'] = str (obj.media.name)
		return  response

class ProductListView(ListView):
	model= Product

	def get_queryset(self,*args,**kwargs):
		qs= super(ProductListView,self).get_queryset(*args,**kwargs)
		#qs=qs.order_by('-price')
		query= self.request.GET.get("q","")
		qs=qs.filter(Q(title__icontains=query)| Q(description__icontains=query)).order_by("-price")
		return qs
	

	# def get_context_data(self,*args,**kwargs):
	# 	context= super(ProductListView, self).get_context_data(**kwargs)
	# 	context["queryset"] = Product.objects.all()
	# 	return context
    



# def product_create_form(request):
	
# 	form = ProductModelForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()

# 	template= "form.html"
# 	context={
# 	   'form' : form,
# 	   'submit_btn': 'create',
# 	}
# 	return render (request, template, context)






# def detail_view(request,object_id=None):
# #	if object_id is not None:
# #		try:
# #			product = Product.objects.get(id=object_id)
# #		except:
# #			product= None
# 		product = get_object_or_404(Product,id=object_id)	

# 		template="detail_view.html"
# 		context={
# 		'instance': product,

# 				}
# 		return render(request,template,context)
# #	else:
# #		return Http404


# def update_view(request,object_id=None):

# 	product = get_object_or_404(Product,id=object_id)
# 	form = ProductModelForm(request.POST or None,instance=product)
# 	if form.is_valid():
# 		form.save()
# 	template="form.html"
# 	context={
# 	'instance': product,
# 	'form':form,
# 	'submit_btn': 'update'
# 	}
# 	return render(request,template,context)



# def detail_slug_view(request,slug=None):
# 	product= get_object_or_404(Product, slug=slug)

# 	template="detail_view.html"
		
# 	context={
# 		'instance': product,
# 		}
# 	return render(request,template,context)

	
		



# def list_view(request):
# 	print request
# 	queryset= Product.objects.all()
# 	template="list_view.html"
# 	context={
# 	'instance': queryset,
# 	}
# 	return render(request,template,context)	