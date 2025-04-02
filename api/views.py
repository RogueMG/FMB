from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, TiffinSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Tiffin

# Create your views here.

class TiffinListCreate(generics.ListCreateAPIView):
    serializer_class = TiffinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tiffin.objects.filter(incharge=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(incharge=self.request.user)
        else:
            print(serializer.errors)

class TiffinRecords(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TiffinSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tiffin.objects.filter(incharge=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

