from accounts.models.users import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import ListAPIView,CreateAPIView
from accounts.serializers.user import UserSerializer
from utils.views import gen_otp,send_sms
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView


class GetUserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class CreateUserAPIView(CreateAPIView):
#     def post(self, request,*args,**kwargs):
#         instance = UserSerializer(data=request.data)
#         if instance.is_valid():
#             User.objects.create(email=instance.data['email'],mobile_number=instance.data['mobile_number'],date_joined=instance.data['date_joined'],otp=instance.data['otp'],login_type=instance.data['login_type'])
#             return Response(instance.data)
#         else:
#             return Response(instance.errors)
        
class CreateUserAPIView(CreateAPIView):
    def post(self, request,*args,**kwargs):
        email = request.data.get('email')
        mobile_number = request.data.get('mobile_number')
        date = request.data.get('date_joined')
        otp = request.data.get('otp')
        login_type = request.data.get('login_type')
        password = request.data.get('password')

        if email and mobile_number and date and otp and login_type and password:
            try:
                password_hash = make_password(password)
                user = User.objects.create(email=email, mobile_number=mobile_number, date_joined=date, otp=otp, login_type=login_type, password=password_hash)
                instance = UserSerializer(user)
                return Response(instance.data)
            except User.DoesNotExist:
                return Response({"message": "User creation failed"})
        else:
            return Response({"message": "Provide all details of the user"})
        

class SendOTPAPiView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        mobile_number = request.data.get('mobile_number')
        if mobile_number:
            user = User.objects.filter(mobile_number=mobile_number)
            if user:
                otp = gen_otp()
                send_sms(phone_number = mobile_number, OTP = otp)
                user.update(otp=otp)
                return Response({'message':"OTP Send Successfully"})
            else:
                return Response({'message':"Enter the right phone number"})
        else:
            return Response({'message':"You are not a valid Register user"})

class LoginVerifyAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        login_type = request.data.get('login_type')
        if login_type == "mobile":
            return self.mobile_login(request)
        elif login_type == "email":
            return self.email_login(request)
        else:
            return Response({'message': "Invalid login type"})

    def mobile_login(self, request,*args,**kwargs):
        mobile_number = request.data.get('mobile_number')
        otp = request.data.get('otp')
        try:
            user = User.objects.get(mobile_number=mobile_number,otp=otp)
            if user:
                refresh = RefreshToken.for_user(user)
                token = {'refresh': str(refresh),'access': str(refresh.access_token),}
                return Response(token)
            else:
                return Response({'message':'Wrong OTP'})
        except User.DoesNotExist:
            return Response({'message':'User does not exist'})
    
    def email_login(self,request,*args,**kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                token = {'refresh': str(refresh),'access': str(refresh.access_token),}
                return Response(token)
            else:
                return Response({"message": "Incorrect password"})
        except User.DoesNotExist:
            return Response({"message": "User not found"})
