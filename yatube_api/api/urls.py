from django.urls import include, path
from rest_framework import routers

from . import views
from .views import FollowViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    path('v1/posts/<int:pk>/', views.api_posts_detail),
    path('v1/groups/', views.api_groups),
    path('v1/groups/<int:pk>/', views.api_groups_detail),
    path('v1/posts/<int:pk>/comments/', views.api_posts_detail_comments),
    path(
        'v1/posts/<int:post_pk>/comments/<int:comment_pk>/',
        views.api_posts_detail_comments_detail
    ),
]
