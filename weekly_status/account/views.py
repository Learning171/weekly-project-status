from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import (
    UserRegistartionSerializers,
    UserLoginSerializer,
    UserProfileSerializer,
    UserChangePasswordSerializer,
    SendPasswordResetEmailSerializer,
    UserPasswordResetSerializer,
    UserLogoutSerializer,
)
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# Generate token Manully
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserRegistartionView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistartionSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response(
            {"token": token, "msg": "Registration Successful"},
            status=status.HTTP_201_CREATED,)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_email = serializer.data.get("user_email")
        password = serializer.data.get("password")
        user = authenticate(user_email=user_email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({"token": token, "msg": "Login Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": {"non_field_errors": ["Email and password is not Valid"]}},
                status=status.HTTP_400_BAD_REQUEST,)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Change Successful"}, status=status.HTTP_201_CREATED)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password reset link send. Please Check your Email"},
            status=status.HTTP_200_OK,)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={"uid": uid, "token": token})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password reset Successfully"}, status=status.HTTP_200_OK)
    
class UserLogoutView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        try:
            serializer = UserLogoutSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            token = get_tokens_for_user(user)
            token.blacklist()
            return Response({"msg": "Logout Successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
