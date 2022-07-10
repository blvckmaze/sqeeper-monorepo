from django.urls import path
from . import api

urlpatterns = [
    path("create/", api.CreateApi.as_view(), name="create"),
    path("update/<int:note_id>", api.UpdateApi.as_view(), name="update"),
    path("delete/<int:note_id>", api.DeleteApi.as_view(), name="delete"),
    path("view/all", api.ViewAllApi.as_view({"get": "list"}), name="list_all_notes"),
]
