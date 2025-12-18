from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import UserProfile, Team, Activity, Workout, Leaderboard

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class WorkoutSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration_minutes', 'created_by', 'created_at']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'score', 'last_updated']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'created_at']


class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'distance_km', 'timestamp']
