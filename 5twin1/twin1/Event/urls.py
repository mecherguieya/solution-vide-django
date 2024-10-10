#on a creer ce fichier 
from django.urls import path
from .views import hello

urlpatterns = [
    path('hello/', hello),
]