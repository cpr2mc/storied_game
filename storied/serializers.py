from django.contrib.auth.models import User
from rest_framework import serializers
from storied.models import Story, StoryTile, CharacterPlayer

class StorySerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='storied:user-detail', read_only=True)
    class Meta:
        model = Story
        fields = ['id', 'name', 'play_date', 'owner']

class StoryTileSerializer(serializers.ModelSerializer):
    story = serializers.HyperlinkedRelatedField(view_name='storied:story-detail', read_only=True)

    class Meta:
        model = StoryTile
        fields = ['id', 'x_coord', 'y_coord', 'prompt', 'enemy_tile', 'story']

class UserSerializer(serializers.ModelSerializer):
    stories = serializers.HyperlinkedRelatedField(many=True, queryset=Story.objects.all(), view_name='storied:story-detail')

    class Meta:
        model = User
        fields = ['id', 'username', 'stories']