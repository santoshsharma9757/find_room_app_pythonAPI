from django.urls import path
from .views import RoomView,RoomDetailView,UserRoomsAPIView

urlpatterns = [
    path("room/", RoomView.as_view()),
    path('room/<uuid:pk>/',RoomDetailView.as_view()),
    path('room/user/<uuid:user_id>/',UserRoomsAPIView.as_view()),
]
