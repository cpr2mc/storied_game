from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from storied.models import StoryTile, Story
from storied.serializers import StorySerializer, StoryTileSerializer, UserSerializer
from storied.permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('storied:user-list', request=request, format=format),
        'stories': reverse('storied:story-list', request=request, format=format),
        'story-tiles': reverse('storied:story-tiles', request=request, format=format)
    })

class StoryRender(generics.GenericAPIView):
    queryset = Story.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        story = self.get_object()
        return Response(story.name)

class StoryList(generics.ListCreateAPIView):
    '''
    List all stories, or create a new story.
    '''
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    List all stories, or create a new story.
    '''
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class StoryTileList(generics.ListCreateAPIView):
    '''
    List all story tiles, or create a new story tile.
    '''
    queryset = StoryTile.objects.all()
    serializer_class = StoryTileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoryTileDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete a code snippet.
    '''
    queryset = StoryTile.objects.all()
    serializer_class = StoryTileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer