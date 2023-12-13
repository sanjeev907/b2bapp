from rest_framework import serializers
from accounts.models.profile import *

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model= Hobby
        fields = '__all__'

class HobbyViewSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class InterestViewSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'

class UserTypeViewSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileViewSerializer(serializers.Serializer):
    dealer_code = serializers.CharField(required=True, error_messages = {'dealer_code': 'dealer_code is required'})
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})
    dob = serializers.DateField(required=True, error_messages = {'dob': 'dob is required'})
    alternate_mobile = serializers.CharField(required=False,)
    aadhar_card = serializers.CharField(required=False)
    aadhar_front_image = serializers.ImageField(required=False)
    aadhar_back_image = serializers.ImageField(required=False) 
    have_kids = serializers.BooleanField(required=False)
    no_of_kids = serializers.BooleanField(required=False)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyViewSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'dealer_code': 'dealer_code is required'})
    comapny_type = serializers.CharField(required=True, error_messages = {'dealer_code': 'dealer_code is required'})
    firm_image= serializers.ImageField(required=False)
    pan_number = serializers.CharField(required=False) 
    gst_in = serializers.CharField(required=False) 
    gst_image = serializers.ImageField(required=False) 