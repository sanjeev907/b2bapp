from django.contrib import admin
from django.urls import path,include
from accounts.views.user import *
urlpatterns = [
    path('get-user',GetUserAPIView.as_view(), name="getallusers"),
    path('create-user',CreateUserAPIView.as_view(), name="create-user"),
    path('send-otp',SendOTPAPiView.as_view(), name="send-otp"),
    path('login',LoginVerifyAPIView.as_view(), name="login"),
]