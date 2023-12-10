from rest_framework import serializers
from accounts.models.family import *

class SpouseSerializer(serializers.ModelSerializer):
    class Meta:
        models = Spouse
        fields = '__all__'

class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Parents
        fields = '__all__'

class KidsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Kids
        fields = '__all__'
