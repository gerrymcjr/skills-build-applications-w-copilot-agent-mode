from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import UserProfile, Team, Activity
from django.utils import timezone

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **options):
        self.stdout.write('Populating test data...')

        # Delete old data
        Activity.objects.all().delete()
        Team.objects.all().delete()
        UserProfile.objects.all().delete()
        User = get_user_model()
        # Djongo workaround: delete non-superuser users one by one
        for user in User.objects.all():
            if not user.is_superuser:
                user.delete()

        # Superhero users
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'bio': 'Genius, billionaire, playboy, philanthropist.'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'bio': 'The First Avenger.'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'bio': 'Friendly neighborhood Spider-Man.'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'bio': 'The Dark Knight.'},
            {'username': 'superman', 'email': 'superman@dc.com', 'bio': 'Man of Steel.'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'bio': 'Amazonian warrior princess.'},
        ]

        marvel_users = []
        dc_users = []
        for hero in marvel_heroes:
            user, created = User.objects.get_or_create(username=hero['username'], defaults={'email': hero['email']})
            if created:
                user.set_password('password')
                user.save()
            marvel_users.append(user)
            UserProfile.objects.get_or_create(user=user, defaults={'bio': hero['bio']})

        for hero in dc_heroes:
            user, created = User.objects.get_or_create(username=hero['username'], defaults={'email': hero['email']})
            if created:
                user.set_password('password')
                user.save()
            dc_users.append(user)
            UserProfile.objects.get_or_create(user=user, defaults={'bio': hero['bio']})

        # Create teams
        marvel_team, _ = Team.objects.get_or_create(name='Team Marvel')
        marvel_team.members.set(marvel_users)
        marvel_team.save()

        dc_team, _ = Team.objects.get_or_create(name='Team DC')
        dc_team.members.set(dc_users)
        dc_team.save()

        # Create activities
        Activity.objects.create(user=marvel_users[0], activity_type='run', duration_minutes=40, distance_km=10.0, timestamp=timezone.now())
        Activity.objects.create(user=marvel_users[1], activity_type='cycle', duration_minutes=60, distance_km=25.0, timestamp=timezone.now())
        Activity.objects.create(user=marvel_users[2], activity_type='walk', duration_minutes=30, distance_km=3.0, timestamp=timezone.now())
        Activity.objects.create(user=dc_users[0], activity_type='run', duration_minutes=50, distance_km=12.0, timestamp=timezone.now())
        Activity.objects.create(user=dc_users[1], activity_type='swim', duration_minutes=35, distance_km=2.0, timestamp=timezone.now())
        Activity.objects.create(user=dc_users[2], activity_type='cycle', duration_minutes=70, distance_km=30.0, timestamp=timezone.now())

        self.stdout.write(self.style.SUCCESS('Populated octofit_db with superhero users, profiles, teams, and activities'))
