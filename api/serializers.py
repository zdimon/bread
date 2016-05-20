from rest_framework import serializers
from api.models import *

# Serializers define the API representation.
class KioskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kiosk
        fields = ('url','address', 'latitude', 'longitude')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    subcategory = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ('url','name', 'subcategory', 'category')


class HightLevelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

