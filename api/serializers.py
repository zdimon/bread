from rest_framework import serializers
from api.models import *

# Serializers define the API representation.
class KioskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kiosk
        fields = ('url','address', 'latitude', 'longitude')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategory_product = serializers.StringRelatedField(many=True)
    category_product = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ('url','name', 'subcategory_product', 'category_product')


class HightLevelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class DetailCategorySerializer(serializers.ModelSerializer):
    #children = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ('id','name', 'category_product', 'subcategory_product', 'children')
        depth = 2


