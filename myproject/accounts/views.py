from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Connexion réussie', 'user_id': user.id}, status=status.HTTP_200_OK)
        return Response({'error': 'Identifiants invalides'}, status=status.HTTP_400_BAD_REQUEST)
    
from django.shortcuts import render

def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

def home_page(request):
    return render(request, 'home.html')