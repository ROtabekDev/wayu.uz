from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer

from .models import Country

class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = ('name', 'flag')