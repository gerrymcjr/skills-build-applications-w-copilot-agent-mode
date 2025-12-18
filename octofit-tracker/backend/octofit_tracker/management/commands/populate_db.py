from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import UserProfile, Team, Activity
from django.utils import timezone

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **options):
        self.stdout.write('Populating test data...')

        # Create users
        users = []
        for i in range(1, 4):
            username = f'user{i}'
            user, created = User.objects.get_or_create(username=username, defaults={
                'email': f'{username}@example.com',
            })
            if created:
                user.set_password('password')
                user.save()
            users.append(user)

        # Create profiles
        for user in users:
            UserProfile.objects.get_or_create(user=user, defaults={'bio': f'Test bio for {user.username}'})

        # Create team and add members
        team, _ = Team.objects.get_or_create(name='Team Alpha')
        team.members.set(users)
        team.save()

        # Create activities
        Activity.objects.create(user=users[0], activity_type='run', duration_minutes=30, distance_km=5.0, timestamp=timezone.now())
        Activity.objects.create(user=users[1], activity_type='cycle', duration_minutes=45, distance_km=20.0, timestamp=timezone.now())
        Activity.objects.create(user=users[2], activity_type='walk', duration_minutes=60, distance_km=4.0, timestamp=timezone.now())

        self.stdout.write(self.style.SUCCESS('Populated octofit_db with sample users, profiles, teams, and activities'))
