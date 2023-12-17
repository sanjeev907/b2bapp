from rest_framework import serializers
from accounts.models.profile import *

class HobbySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})


class InterestSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})

class UserTypeSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})


class UserProfileSerializer(serializers.Serializer):
    dealer_code = serializers.CharField(required=True, error_messages = {'dealer_code': 'dealer_code is required'})
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})
    dob = serializers.DateField(required=True, error_messages = {'dob': 'dob is required'})
    alternate_mobile = serializers.CharField(required=False,)
    aadhar_card = serializers.CharField(required=False)
    aadhar_front_image = serializers.ImageField(required=False)
    aadhar_back_image = serializers.ImageField(required=False) 
    have_kids = serializers.BooleanField(required=False)
    no_of_kids = serializers.BooleanField(required=False)


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'dealer_code': 'dealer_code is required'})
    company_type = serializers.CharField(required=True, error_messages = {'dealer_code': 'dealer_code is required'})
    firm_image= serializers.ImageField(required=False)
    pan_number = serializers.CharField(required=False) 
    gst_in = serializers.CharField(required=False) 
    gst_image = serializers.ImageField(required=False) 
