from django.db import models
from django.conf import settings
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Profile for {self.user.username}"


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('run', 'Run'),
        ('cycle', 'Cycle'),
        ('walk', 'Walk'),
        ('swim', 'Swim'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} @ {self.timestamp.date()}"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
