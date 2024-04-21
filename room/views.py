from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class RoomView(APIView):
   
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        # Get the 'district' parameter from the query string
        district = request.query_params.get('district', None)
        # Filter rooms based on the district (modify this according to your model structure)
        print("QUERY PARAM DISTRICT",district)
        if district:
            rooms = Room.objects.filter(district=district)
        else:
            rooms = Room.objects.all()
        print(rooms)
        serializer= RoomSerializer(rooms,many=True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)

    
    def post(self,request,format=None):
        data=request.data
        user = request.user 
        serializer=RoomSerializer(data=data)
        if serializer.is_valid():
          serializer.save(user=user)
          return Response({"message":'Room Posted successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        

class RoomDetailView(APIView):
    def get(self,request,pk,format=None):
        try:
         roomData= Room.objects.get(id=pk)
         serializer= RoomSerializer(roomData)
         print(roomData)
         return Response({'data':serializer.data},status=status.HTTP_200_OK)
        except Room.DoesNotExist:
            return Response({"message": "Room not found"}, status=status.HTTP_404_NOT_FOUND)
        
class UserRoomsAPIView(APIView):
    def get(self, request, user_id, format=None):
        try:
            rooms = Room.objects.filter(user_id=user_id)
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Room.DoesNotExist:
            return Response({'error': 'Rooms not found for the given user ID'}, status=status.HTTP_404_NOT_FOUND)


        




       