from django.urls import include, path
from rest_framework import routers

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowVievSet

router_api_v1 = routers.DefaultRouter()
router_api_v1.register('posts', PostViewSet, basename='post')
router_api_v1.register('groups', GroupViewSet, basename='group')
router_api_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')
router_api_v1.register('follow', FollowVievSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_api_v1.urls)),
]
