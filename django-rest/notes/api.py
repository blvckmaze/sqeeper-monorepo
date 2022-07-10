from .models import Note
from . import serializers, services
from users.auth import CustomUserAuth
# from .paginators import NotesPagination

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet


class CreateApi(APIView):
    authentication_classes = (CustomUserAuth,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = serializers.NoteSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_note(user=request.user, note=data)

        return Response(serializer.data)


class UpdateApi(APIView):
    authentication_classes = (CustomUserAuth,)
    permission_classes = (IsAuthenticated,)

    def patch(self, request, note_id):
        serializer = serializers.UpdateNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        serializer.instance = services.update_note(
            user=request.user, note_id=note_id, note_data=data
        )

        return Response(data=serializer.data)


class DeleteApi(APIView):
    authentication_classes = (CustomUserAuth,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, note_id):
        services.delete_note(user=request.user, note_id=note_id)
        return Response(status=HTTP_204_NO_CONTENT)


class ViewAllApi(ReadOnlyModelViewSet):
    authentication_classes = (CustomUserAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.NoteSerializer
    # pagination_class = NotesPagination

    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["created"]
    ordering = ["-created"]
    search_fields = ["title", "description"]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
