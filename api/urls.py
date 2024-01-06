from django.urls import path
from .views import  note_list, note, search_notes, share_notes
from .auth_views import register_user, user_login

urlpatterns = [
    path('auth/signup/', register_user, name='register_user'),
    path('auth/login/', user_login, name='user_login'),
    path('notes/', note_list, name='note_list'),
    path('notes/<int:pk>/', note, name='note-detail'), 
    path('search/', search_notes, name='note-search'), 
    path('notes/<int:pk>/share/', share_notes, name='note-share'), 
    
]