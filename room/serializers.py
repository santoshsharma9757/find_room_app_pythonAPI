from rest_framework import serializers
from .models import Room, RoomImages
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','mobile']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    gallery_images = RoomImageSerializer(many=True, read_only=True)
    images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    user = UserSerializer(read_only=True)
    class Meta:
        model = Room
        fields = ['id','city','user','district','address', 'price', 'description', 'gallery_images', 'images']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        uploaded_images = validated_data.pop("images")
        room = Room.objects.create(**validated_data)

        for image in uploaded_images:
            RoomImages.objects.create(room=room, image=image)

        return room
