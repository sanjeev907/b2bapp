from django.contrib import admin
from django.urls import path,include
from accounts.views.user import *
from accounts.views.profile import *
urlpatterns = [
    path('get-user',GetUserAPIView.as_view(), name="getallusers"),
    path('create-user',CreateUserAPIView.as_view(), name="create-user"),
    path('send-otp',SendOTPAPiView.as_view(), name="send-otp"),
    path('login',LoginVerifyAPIView.as_view(), name="login"),
    path('hobby',GetHobbyAPIView.as_view(), name="hobby"),
    path('create-hobby',CreateHobbyAPIView.as_view(), name="create-hobby"),
    path('interest',GetInterestAPIView.as_view(), name="interest"),
    path('create/interest',CreateInterestAPIView.as_view(), name="create-interest"),
    path('user-type',GetUserTypeAPIView.as_view(), name="user-type"),
    path('profile',GetUserProfiledAPIView.as_view(), name="profile"),
    path('create/profile',CreateUserProfileView.as_view(), name="create-profile"),
    path('update/profile/<int:id>',UpdateUserProfileAPIView.as_view(), name="update-profile"),
    path('company',GetCompanyAPIView.as_view(), name="company"),
    path('create/company',CreateComapanyAPIView.as_view(), name="create-company"),
    path('update/company/<int:id>',UpdateCompanyDetailsAPIView.as_view(), name="update-company"),
]