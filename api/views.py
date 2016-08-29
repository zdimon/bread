from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def hello_world(request):
    return Response({"message": "Hello, world!"})




class KioskViewSet(viewsets.ModelViewSet):
    queryset = Kiosk.objects.all()
    serializer_class = KioskSerializer




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @list_route()
    def directory(self, request, *args, **kwargs):
        #subdirectory = self.get_object() if detail_route
        #serializer = HightLevelCategorySerializer(subdirectory,context={'request': request})
        serializer = HightLevelCategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


    @detail_route()
    def directory_detail(self, request, *args, **kwargs):
        directory = self.get_object()
        serializer = DetailCategorySerializer(directory,context={'request': request})
        return Response(serializer.data)


