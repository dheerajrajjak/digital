"""digitalmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("products.urls", namespace="products")),    

]

# if settings.DEBUG:
#     urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # url(r'^detail/(?P<object_id>\d+)/$', 'products.views.detail_view',name="detail_view"),
    # url(r'^detail/(?P<object_id>\d+)/edit$', 'products.views.update_view',name="update_view"),    
    # url(r'^detail/(?P<slug>[\w-]+)/$', 'products.views.detail_slug_view',name="detail_slug_view"),
    # url(r'^create/$','products.views.product_create_form',name="create_form"),
    # url(r'^list/$','products.views.list_view',name="list_view"),