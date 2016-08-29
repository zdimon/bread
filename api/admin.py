from django.contrib import admin

from api.models import *
from image_cropping import ImageCroppingMixin
from mptt.admin import MPTTModelAdmin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_slug', 'thumb', 'price', 'rate', 'category', 'subcategory', 'ammount')
    list_filter = ('name', 'price', 'rate')
    list_editable = ('ammount',)


class KioskAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('address', 'name', 'pub')
    search_fields = ['name', 'address']
    list_editable = ('pub',)

class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'name_slug', 'level', 'parent')


class ProductImagesAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('thumb', 'product', 'is_main')


admin.site.register(ProductImages, ProductImagesAdmin)
admin.site.register(Kiosk, KioskAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
