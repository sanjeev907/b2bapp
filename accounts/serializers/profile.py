from rest_framework import serializers
from accounts.models.profile import *

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        models = Hobby
        fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        models = Interest
        fields = '__all__'

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserType
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserProfile
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        models = Company
        fields = '__all__'