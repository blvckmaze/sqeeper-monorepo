from rest_framework import serializers
from .services import UserData
from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def to_internal_value(self, data):
        return UserData(**super().to_internal_value(data))
