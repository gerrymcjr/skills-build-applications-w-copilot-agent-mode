"""octofit_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os
from .views import UserViewSet, UserProfileViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)



@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    base_url = request.build_absolute_uri('/')
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev/'
    api_url = lambda path: base_url.rstrip('/') + path
    return Response({
        'users': api_url(reverse('user-list', request=request, format=format)),
        'profiles': api_url(reverse('userprofile-list', request=request, format=format)),
        'teams': api_url(reverse('team-list', request=request, format=format)),
        'activities': api_url(reverse('activity-list', request=request, format=format)),
        'workouts': api_url(reverse('workout-list', request=request, format=format)),
        'leaderboard': api_url(reverse('leaderboard-list', request=request, format=format)),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
