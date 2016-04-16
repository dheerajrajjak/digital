
from django.conf.urls import include, url
from django.contrib import admin
from .views import (
	ProductListView,
	ProductDetailView, 
	ProductCreateView, 
	ProductUpdateView,
	ProductDownloadView,
	)


urlpatterns = [
      
    url(r'^list/$',ProductListView.as_view(),name="List"),
    url(r'^create/$',ProductCreateView.as_view(),name="Create"),
    url(r'^update/(?P<pk>\d+)$',ProductUpdateView.as_view(),name="Update"),
    url(r'^detail/(?P<pk>\d+)$',ProductDetailView.as_view(),name="Detail"),
    url(r'^detail/(?P<pk>\d+)/download/$',ProductDownloadView.as_view(),name="Download"),
    url(r'^detail/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(),name="detail_slug"),
   
    

]


 