from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
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

class StoryViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions.
    '''
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StoryTileViewSet(viewsets.ModelViewSet):
    queryset = StoryTile.objects.all()
    serializer_class = StoryTileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automatically provides 'list' and 'retrieve' actions for Users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer