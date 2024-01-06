from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, NoteSerializer 
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from django.db import models
from django_ratelimit.decorators import ratelimit

###################################################--SIGNUP VIEWSET--##########################################################################

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###################################################--LOGIN VIEWSET--##########################################################################

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # print("random string")

    user = CustomUser.objects.filter(username=username).first()


    if user and password == user.password:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)