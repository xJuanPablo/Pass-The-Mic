from django.shortcuts import render
from rest_framework import generics
from .serializers import AudioArenaSerializer
from .models import AudioArena

class AudioArenaView(generics.CreateAPIView):
  queryset = AudioArena.objects.all()
  serializer_class = AudioArenaSerializer