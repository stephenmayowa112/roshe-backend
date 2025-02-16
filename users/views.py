from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Mentor, Mentee, Review
from .models import Session  
from .serializers import MentorSerializer, MenteeSerializer, SessionSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Login successful"})
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
# class UserLoginView(TokenObtainPairView):
#     pass  # Default view for obtaining JWT

class TokenRefreshView(TokenRefreshView):
    pass  # Default view for refreshing JWT token

class MentorListView(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MenteeListView(generics.ListCreateAPIView):
    queryset = Mentee.objects.all()
    serializer_class = MenteeSerializer

class MenteeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentee.objects.all()
    serializer_class = MenteeSerializer
    
class SessionListView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
