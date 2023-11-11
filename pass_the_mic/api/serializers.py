# This file takes AudioArena model and translate the fields into a json response

from rest_framework import serializers
from .models import AudioArena

class AudioArenaSerializer(serializers.ModelSerializer):
  class Meta: 
    model = AudioArena
    fields = ('id','code', 'host', 'guest_can_pause','votes_to_skip', 'created_at')