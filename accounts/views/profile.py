from accounts.models.users import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView,CreateAPIView
from accounts.serializers.profile import *
from accounts.models.profile import *

class GetHobbyAPIView(ListAPIView):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

class CreateHobbyAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        if name:
            hobby = Hobby.objects.create(name=name)
            instance = HobbyViewSerializer(hobby)
            return Response(instance.data)
        else:
            return Response({'message':'Enter Your Hobby Name'})
        


class GetInterestAPIView(ListAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class GetUserTypeAPIView(ListAPIView):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

class GetUserProfiledAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GetCompanyAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer