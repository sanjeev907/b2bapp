from rest_framework import serializers
from accounts.models.users import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'mobile_number', 'date_joined', 'otp', 'login_type', 'password')
        abstract = True
