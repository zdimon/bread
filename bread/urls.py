"""bread URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import detail_route, list_route
from api.models import *
from api.views import *
from api.serializers import *



# ViewSets define the view behavior.
class KioskViewSet(viewsets.ModelViewSet):
    queryset = Kiosk.objects.all()
    serializer_class = KioskSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'kiosk', KioskViewSet)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(level=0)
    serializer_class = CategorySerializer

    @list_route()
    def subdirectory(self, request, *args, **kwargs):
        #subdirectory = self.get_object() if detail_route
        #serializer = HightLevelCategorySerializer(subdirectory,context={'request': request})
        serializer = HightLevelCategorySerializer(self.queryset, many=True)
        return Response(serializer.data)



router.register(r'category', CategoryViewSet)




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello_world),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
