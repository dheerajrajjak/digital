from django.contrib import admin

# Register your models here.
from .models import Product, Thumbnail


class ThumbnailInline(admin.TabularInline):
	model= Thumbnail


class ProductAdmin(admin.ModelAdmin):
	inlines = [ThumbnailInline]
	list_display=["__unicode__","description","price"]
	search_fields=["description"]
	class Meta:
		model= Product


admin.site.register(Thumbnail)
admin.site.register(Product, ProductAdmin)