from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tiffin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class TiffinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiffin
        fields = ["id", "tiffin_number", "tiffin_mohalla", "payment_status", "incharge", "last_updated"]
        extra_kwargs = {
            "incharge": {"read_only": True},
            "last_updated": {"read_only": True}
            }