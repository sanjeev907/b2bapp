from rest_framework import serializers
from accounts.models.family import *

class SpouseSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages={'name': 'name is required'})
    dob = serializers.DateField(required=True, error_messages={'dob': 'dob is required'})
    doa = serializers.DateField(required=True, error_messages={'doa': 'doa is required'})
    profession = serializers.CharField(required=False)
    mobile =  serializers.CharField(required=False)
    email = serializers.CharField(required=False)


class ParentsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages={'name': 'name is required'})
    parent = serializers.CharField(required=True, error_messages={'parent': 'parent is required'})
    dob = serializers.DateField(required=True, error_messages={'dob': 'dob is required'})
    

class KidsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages={'name': 'name is required'})
    dob = serializers.DateField(required=True, error_messages={'dob': 'dob is required'})
    gender = serializers.CharField(required=True, error_messages={'gender': 'gender is required'})