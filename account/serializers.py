from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':"password"},write_only=True)
    class Meta:
        model=User
        fields=['name','email','mobile','city','district','address','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def validate(self, attrs):
        password=attrs.get("password")
        password2=attrs.get("password2")
        print("PASSWORD1",password),
        print("PASSWORD2",password2)
        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't matched")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class UserLoginSerializer(serializers.ModelSerializer):
     email=serializers.EmailField(max_length=255)
     class Meta:
        model=User
        fields=['id','email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','mobile']        


    



