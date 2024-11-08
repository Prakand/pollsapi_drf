from rest_framework.views import APIView
from .serializers import PollSerializer,VoteSerializer,ChoiceSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class PollList(APIView):
    def get(self,request):
        polls = Poll.objects.all()
        data = PollSerializer(polls,many=True).data
        return Response(data)
    
class PollDetail(APIView):
    def get(self,request,pk):
        poll = get_object_or_404()
        data = PollSerializer(poll).data
        return Response(data)
    

class LoginView(APIView):

    permission_classes=()
    def post(self,request):
        username = request.get.data("username")
        password = request.get.data("password")
        user = authenticate(username=username, password = password)

        if user:
            return Response({"token": user.auth_token.key},status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid credentials"},status=status.HTTP_404_NOT_FOUND)

class RegisterView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password or not email:
            raise ValidationError("Username, email, and password are required.")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)



class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Assuming you're using token-based authentication
        request.auth.delete()  # Delete the user's token
        return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)