from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserSerializer, NoteSerializer 
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django_ratelimit.exceptions import Ratelimited
from django.db.models import Q
from .models import CustomUser, Note
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db import models
from django_ratelimit.decorators import ratelimit

###################################################--CREATE AND READ NOTES--##########################################################################

@ratelimit(key='user',rate = '15/h', block = True)
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def note_list(request):
    if request.method == 'GET':
        user  =  request.user
        owned_notes = Note.objects.filter(created_by = user)
        shared_notes = Note.objects.filter(shared_users = user)
        notes = owned_notes | shared_notes
        if notes:
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data)
        else:
            return Response({"Message" : "You dont have any notes to view"}, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        created_by = request.user
        serializer_data = request.data
        serializer_data['created_by'] = request.user.id
        serializer = NoteSerializer(data = serializer_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

####################################################--READ, UPDATE AND DELETE NOTES BY ID--#########################################################################

@ratelimit(key='user',rate = '15/h', block = True)
@api_view(['GET', 'PUT','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def note(request,pk):
    if request.method == 'GET':
        user  =  request.user
        owned_notes = Note.objects.filter(created_by = user)
        shared_notes = Note.objects.filter(shared_users = user)
        notes = owned_notes | shared_notes
        print(notes)

        if notes :
            notes = notes.filter(id= pk)
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message" : "You dont have notes to view"}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        user  =  request.user
        note = get_object_or_404(Note, created_by=user, id=pk)

        if not request.data['title']:
            if request.data['content']:
                pass
            else:
                return Response({"Message": "No changes Made"})
            request.data['title'] = note.title
       
        if not request.data['content']:
            request.data['content'] = note.content

        serializer_data = request.data
      
        serializer_data['created_by'] = request.user.id
        serializer = NoteSerializer(note,data = serializer_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
    elif request.method == 'DELETE':
        user = request.user
        note = get_object_or_404(Note, created_by=user, id=pk)
        note.delete()
        return Response({"Message": "Note Succesfuly Deleted"},status=status.HTTP_204_NO_CONTENT)
        

################################################--SEARCH NOTES USING QUERY--#############################################################################

@ratelimit(key='user',rate = '3/h', block = True)
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def search_notes(request):
    try :
    
        user = request.user
        query = request.query_params.get('q', '')
        owned_notes = Note.objects.filter(created_by = user)
        shared_notes = Note.objects.filter(shared_users = user)
        notes = owned_notes | shared_notes

        if not query:
            return Response({"detail": "Query parameter 'q' is required."}, status=status.HTTP_400_BAD_REQUEST)

        notes = notes.filter( models.Q(title__trigram_similar=query) | models.Q(content__trigram_similar=query))
        print(notes.filter( models.Q(title__trigram_similar=query) | models.Q(content__trigram_similar=query)).explain(analyze=True))
        if notes :
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Such Note Found"}, status =status.HTTP_404_NOT_FOUND )
    except Ratelimited as e:
        return JsonResponse({'error': 'Rate limit exceeded'}, status=429)

################################################--SHARE NOTES--#############################################################################
@ratelimit(key='user',rate = '10/h', block = True)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def share_notes (request, pk):
    user = CustomUser.objects.filter(username=request.data['username'])
    if user:
        try:
            note = Note.objects.filter(created_by = request.user, id=pk)
            if note:
                note[0].shared_users.add(user[0].id)
                return Response({'message': 'Note shared successfully.'})
            else:
                return Response({"error": "Check note ID"},status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": e})
    else:
        return Response({"error": "CHeck Username"},status=status.HTTP_404_NOT_FOUND)


