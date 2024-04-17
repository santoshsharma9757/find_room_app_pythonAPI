from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# from .renderers import UserRenderer
from .models import *

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.

class UserRegisterView(APIView):
#     renderer_classes=[UserRenderer]
    def post(self,request,format=None):
         data=request.data
         serializer=UserRegistrationSerializer(data=data)
         if serializer.is_valid():
              serializer.save()
              return Response({"data":"user register successfully"},status=status.HTTP_200_OK)
         else:
              return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
              

class UserLoginView(APIView):
     # renderer_classes=[UserRenderer]
     def post(self,request,format=None):
          serializer=UserLoginSerializer(data=request.data)
          if serializer.is_valid():
               email=serializer.data.get("email")
               password=serializer.data.get("password")
               user=authenticate(email=email,password=password)
               token=get_tokens_for_user(user)
               if user is not None:
                     return Response({"message":"Login successfully", "user":serializer.data.get("id"),  'token':token},status=status.HTTP_200_OK)
               else:
                return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
          else:
               return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
          
class CityView(APIView):
     def get(self,request,formate=None):
          data = CITY_CHOICES
          result = [item[0] for item in data]
          return Response({"data":result},status=status.HTTP_200_OK)     

class DistrictView(APIView):
     def get(self,request,formate=None):
          data = District_CHOICES
          result = [item[0] for item in data]
          return Response({"data":result},status=status.HTTP_200_OK)            


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

               
        