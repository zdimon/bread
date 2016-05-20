##Cropping

    django-image-cropping==0.8.3
    easy-thumbnails==2.1

###Setting

    MEDIA_URL = '/media/'

    INSTALLED_APPS = [
        ...
        'easy_thumbnails',
        'image_cropping'
    ]

###Url

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

### Model

    from image_cropping import ImageRatioField

    class Blabla(models.Model):
    foto = models.ImageField(upload_to='media', null=True, blank=True)
    cropping = ImageRatioField('foto', '430x360')

### Admin

    from image_cropping import ImageCroppingMixin

    class KioskAdmin(ImageCroppingMixin, admin.ModelAdmin):
