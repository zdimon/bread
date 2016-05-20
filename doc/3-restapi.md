##REST API


###Requirements

    djangorestframework==3.3.3
    django-filter==0.13.0
    markdown==2.6.6

### Configuration

    INSTALLED_APPS = (
        ...
        'rest_framework',
    )

### Url

    from rest_framework import routers, serializers, viewsets
    from api.models import Kiosk

    # Serializers define the API representation.
    class KioskSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Kiosk
            fields = ('url','address', 'latitude', 'longitude')

    # ViewSets define the view behavior.
    class KioskViewSet(viewsets.ModelViewSet):
        queryset = Kiosk.objects.all()[0:20]
        serializer_class = KioskSerializer

    # Routers provide an easy way of automatically determining the URL conf.
    router = routers.DefaultRouter()
    router.register(r'kiosk', KioskViewSet)


    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^', include(router.urls)),...

