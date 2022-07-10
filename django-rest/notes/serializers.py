from users.serializer import UserSerializer
from rest_framework import serializers
from .services import NoteData
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    created = serializers.DateTimeField(format="%d %b %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%d %b %H:%M:%S", required=False)

    class Meta:
        model = Note
        fields = "__all__"

    def to_internal_value(self, data):
        return NoteData(**super().to_internal_value(data))


class UpdateNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = ("owner",)

    def to_internal_value(self, data):
        return NoteData(**super().to_internal_value(data))
