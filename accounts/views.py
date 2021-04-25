from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from .serializers import RegisterUserSerializer

# Create your views here.

class CustomUserCreate(APIView):

    def post(self, request):
        reg_Serializer = RegisterUserSerializer(data=request.data)
        if reg_Serializer.is_valid():
            newuser = reg_Serializer.save()
            if newuser:
                return Response({"success": "Register Successfully..."},status=status.HTTP_201_CREATED)
        return Response(reg_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)