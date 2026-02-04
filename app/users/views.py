from django.shortcuts import render
from rest_framework import  generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer
from rest_framework.views import  APIView
from django.contrib.auth import authenticate

User = get_user_model()

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class LoginView(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
            response = {
                'message':"Login Successfull",
                "token":user.auth_token.key
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data={'message':'Email veya parola yanlıştır.'},status=status.HTTP_400_BAD_REQUEST)



