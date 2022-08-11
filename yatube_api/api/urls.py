from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)

from .views import *

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'follow', FollowViewSet, basename='follows')
router_v1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

jwt_patterns = [
    path('create/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view())
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/jwt/', include(jwt_patterns)),
]
