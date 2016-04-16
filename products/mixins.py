from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404




class SubmitMixin(object):
	submit_btn=None

	def get_context_data(self,*args, **kwargs):
		context= super(SubmitMixin, self).get_context_data(**kwargs)
		context['submit_btn'] = self.submit_btn
		return context

	
class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self,request,*args,**kwargs):
		return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)


class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self,request,*args,**kwargs):
		return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)	


class ProductManagerMixin(LoginRequiredMixin, object):
	def get_object(self, *args,**kwargs):
		user= self.request.user
		obj=super(ProductManagerMixin,self).get_object(*args,**kwargs)
		try:
		 obj.user == user
		except:
			raise Http404
		try:
			user in obj.group.all()
		except:
			raise Http404

		if obj.user==user or obj in obj.group.all():
			return obj
		else:
			return Http404			


