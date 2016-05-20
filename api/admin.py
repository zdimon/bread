from django.contrib import admin

from api.models import *
from image_cropping import ImageCroppingMixin
from mptt.admin import MPTTModelAdmin


class KioskAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('address', 'name', 'pub')
    search_fields = ['name', 'address']
    list_editable = ('pub',)

class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'name_slug', 'level', 'parent')


admin.site.register(Kiosk, KioskAdmin)
admin.site.register(Category, CategoryAdmin)
