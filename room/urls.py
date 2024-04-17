from django.urls import path
from .views import RoomView,RoomDetailView

urlpatterns = [
    path("room/", RoomView.as_view()),
    path('room/<uuid:pk>/',RoomDetailView.as_view()),
]
