from django.urls import path
from . import api

urlpatterns = [
    path("register/", api.RegisterApi.as_view(), name="register"),
    path("login/", api.LoginApi.as_view(), name="login"),
    path("logout/", api.LogoutApi.as_view(), name="logout"),
    path("profile/", api.UserApi.as_view(), name="profile"),
]
