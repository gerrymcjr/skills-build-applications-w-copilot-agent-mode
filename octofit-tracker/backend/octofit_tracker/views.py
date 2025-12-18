from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import UserProfile, Team, Activity
from .serializers import UserSerializer, UserProfileSerializer, TeamSerializer, ActivitySerializer

User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.select_related('user').all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related('members').all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.select_related('user').all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]
