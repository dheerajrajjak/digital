from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files.storage import FileSystemStorage
from digitalmarket import settings
# Create your models here.




def media_image_upload(instance,filename):
	return '%s/%s' %(instance.product.id,filename)

def media_upload_location(instance,filename):
	return '%s/%s' %(instance.id,filename)

class Product(models.Model):
	user= models.ForeignKey(User)
	group=models.ManyToManyField(User, related_name= "product_managers")
	media = models.FileField(blank=True,null=True, upload_to= media_upload_location,
		storage=FileSystemStorage(location= settings.PROTECTED_ROOT)
		)
	title=models.CharField(max_length=30)
	slug=models.SlugField(blank= True)
	description= models.TextField()
	price =models.DecimalField(max_digits=50,decimal_places=2,null=True)


	def __unicode__(self):
		return self.title

 
	def get_absolute_url(self):
		
		return reverse("products:Detail", kwargs={"pk":self.id})

	def get_download(self):
		url= reverse("products:Download", kwargs={"pk": self.id})
		return url
		
		
		


# def pre_save_signal(sender,instance,*args,**kwargs):
# 	if instance.slug == None:
# 		instance.slug= slugify(instance.title)
# 	print instance.slug
# #	if  instance.slug != instance.title:
		
	


# pre_save.connect(pre_save_signal, sender= Product)	


class Thumbnail(models.Model):
	user=models.ForeignKey(User)
	product= models.ForeignKey(Product)
	height= models.CharField(max_length=100, blank=True,null=True)
	width= models.CharField(max_length=100, blank=True,null=True)
	image= models.ImageField(height_field="height", width_field="width", blank=True,null=True,
	 upload_to= media_image_upload)

	def __unicode__(self):
		return str(self.image.path)



