from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from storied import views

app_name = 'storied'
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('stories/', views.StoryList.as_view(), name='story-list'),
    path('stories/detail/<int:pk>', views.StoryDetail.as_view(), name='story-detail'),
    path('stories/<int:pk>/rendered', views.StoryRender.as_view()),
    path('story_tiles/', views.StoryTileList.as_view(), name='story-tiles'),
    path('story_tiles/detail/<int:pk>', views.StoryTileDetail.as_view()),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
])