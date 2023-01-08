from rest_framework import serializers
from .models import Menu, Categorie


""" convert bites modals to json """

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id','name','price','category','image')

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id','name')