from rest_framework import serializers
from .models import CustomUser, Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content','created_by']
# class NoteShareSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Note
#         fields = ['id','shared_users']