from django.urls import path
from .views import PasswordResetView, UserRegisterView,UserLoginView,CityView,DistrictView,UserProfileView

urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("city/", CityView.as_view()),
    path("district/", DistrictView.as_view()),
    path("profile/", UserProfileView.as_view()),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
]
