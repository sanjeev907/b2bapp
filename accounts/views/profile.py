from accounts.models.users import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView,CreateAPIView
from accounts.serializers.profile import *
from accounts.models.profile import *
from rest_framework.permissions import IsAuthenticated


class GetHobbyAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer

class CreateHobbyAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        if name:
            hobby = Hobby.objects.create(name=name)
            instance = HobbySerializer(hobby)
            return Response(instance.data)
        else:
            return Response({'message':'Enter Your Hobby Name'})
        

class GetInterestAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class CreateInterestAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        if name:
            interest = Interest.objects.create(name=name)
            instance = InterestSerializer(interest)
            return Response(instance.data)
        else:
            return Response({'message':'Enter Your Interest Name'})


class GetUserTypeAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

class GetUserProfiledAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CreateUserProfileView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        dealer_code = request.data.get('dealer_code')
        name = request.data.get('name')
        dob = request.data.get('dob')
        try:
            if dealer_code and name and dob:
                user = request.user
                profile = UserProfile.objects.create(user = user ,dealer_code=dealer_code, name=name,dob=dob)
                instance = UserProfileSerializer(profile)
                return Response(instance.data)
            else:
                return Response({'message':'Enter Your All details'})
        except UserProfile.DoesNotExist:
            return Response({'message':'Your are not allowed to create profiles.'})

class UpdateUserProfileAPIView(CreateAPIView):
    def post(self, request,id, *args, **kwargs):
        dealer_code = request.data.get('dealer_code')
        name = request.data.get('name')
        dob = request.data.get('dob')
        try:
                if dealer_code and name and dob:
                    user = request.user
                    profile = UserProfile.objects.get(id=id, user=user)
                    
                    profile.dealer_code = dealer_code
                    profile.name = name
                    profile.dob = dob
                    profile.save()
                    
                    instance = UserProfileSerializer(profile)
                    return Response(instance.data)
                else:
                    return Response({'message':'Invalid User Profile details'})
        except UserProfile.DoesNotExist:
            return Response({'message':'Enter the valid user profile id'})


class GetCompanyAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CreateComapanyAPIView(CreateAPIView):
    def post(self, request,*args,**kwargs):
        name = request.data.get('name')
        company_type = request.data.get('company_type')
        try:
            if name and company_type:
                user = request.user

                company = Company.objects.create(name=name, company_type=company_type, user=user)
                instance = CompanySerializer(company)
                return Response(instance.data)
            else:
                return Response({'message': 'enter the right company details'})
        
        except Company.DoesNotExist:
            return Response({'message': 'Your not enter the right informations details'})
        

class UpdateCompanyDetailsAPIView(CreateAPIView):
    def post(self, request,id, *args, **kwargs):
        name = request.data.get('name')
        company_type = request.data.get('company_type')
        try:
            if name and company_type:
                user = request.user
                company = Company.objects.get(id = id, user = user)
                
                company.name = name
                company.company_type = company_type
                company.save()

                instance = CompanySerializer(company)
                return Response(instance.data)
            else:
                return Response({'message':'Invalid Company details'})
        except UserProfile.DoesNotExist:
            return Response({'message':'Enter the valid Company id'})


            

                
