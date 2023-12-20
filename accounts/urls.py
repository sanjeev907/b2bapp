from django.contrib import admin
from django.urls import path,include
from accounts.views.user import *
from accounts.views.profile import *
from accounts.views.family import *
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
    path('spouse',GetSpouseAPIView.as_view(), name="get-spouse"),
    path('create/spouse',CreateSpouseAPIView.as_view(), name="create-spouse"),
    path('update/spouse/<int:id>',UpdateSpouseAPIView.as_view(), name="update-spouse"),
    path('kids',GetKidsAPIView.as_view(), name="get-kids"),
    path('create/kids',CreateKidsAPIView.as_view(), name="create-kids"),
    path('update/kids/<int:id>',UpdateKidsAPIView.as_view(), name="update-kids"),
    path('parents',GetParentsAPIView.as_view(), name="get-parents"),
    path('create/parent',CreateParentsAPIView.as_view(), name="create-parent"),
    path('update/parent/<int:id>',UpdateParentsAPIView.as_view(), name="update-parent"),
]