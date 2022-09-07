from django.urls import include, path
from rest_framework import routers

from api.auth.views import RegisterView, LoginView
from api.posts.views import PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='pk')


urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]