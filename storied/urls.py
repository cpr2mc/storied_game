from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from storied.views import StoryViewSet, StoryTileViewSet, UserViewSet, api_root

story_list = StoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
story_detail = StoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
story_tile_list = StoryTileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
story_tile_detail = StoryTileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

app_name = 'storied'
urlpatterns = format_suffix_patterns([
    path('api', api_root),
    path('api/stories/', story_list, name='story-list'),
    path('api/stories/detail/<int:pk>', story_detail, name='story-detail'),
    path('api/story_tiles/', story_tile_list, name='story-tiles'),
    path('api/story_tiles/detail/<int:pk>', story_tile_detail, name='storytile-detail'),
    path('api/users/', user_list, name='user-list'),
    path('api/users/<int:pk>/', user_detail, name='user-detail'),
])