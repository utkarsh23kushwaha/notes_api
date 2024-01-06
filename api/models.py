from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique = True)
    def __str__(self):
        return self.username


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shared_users = models.ManyToManyField(CustomUser, related_name='shared_notes')
    search_vector = SearchVectorField(null=True, blank=True)

    class Meta :
        indexes = [GinIndex(name = 'NewGinIndex', fields = ['title', 'content'] , opclasses = ['gin_trgm_ops','gin_trgm_ops'])]

 

    def __str__(self):
        return self.title