import uuid
from django.db import models
from account.models import CITY_CHOICES,District_CHOICES
from account.models import User
# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    city=models.CharField(max_length=200,choices=CITY_CHOICES)
    district=models.CharField(max_length=200,choices=District_CHOICES)
    address=models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='gallery_images')
    image = models.ImageField(upload_to="room_images")