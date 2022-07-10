from rest_framework.response import Response
from rest_framework import views, exceptions, permissions
from . import serializer as user_serializer, services, auth


class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user=data)

        return Response(serializer.data)


class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = services.user_email_selector(email=email)

        if not user or not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid credentials")

        response = Response()

        response.set_cookie(
            key="jwt",
            value=services.user_create_token(uid=user.id),
            httponly=True,
        )

        return response


class LogoutApi(views.APIView):
    authentication_classes = (auth.CustomUserAuth,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        response = Response()

        response.delete_cookie("jwt")
        response.data = {"message": "You have been logged out"}

        return response


class UserApi(views.APIView):
    authentication_classes = (auth.CustomUserAuth,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = user_serializer.UserSerializer(user)

        return Response(serializer.data)
