from rest_framework import serializers
from .models import foods

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = foods
        fields = '__all__'
