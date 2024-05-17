from rest_framework import serializers

from account.models import User
from .models import Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','mobile']




class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=["user","transaction_id"]

