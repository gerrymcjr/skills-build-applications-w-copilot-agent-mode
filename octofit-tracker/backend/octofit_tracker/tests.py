from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth import get_user_model
from .models import UserProfile, Team, Activity, Workout, Leaderboard

User = get_user_model()


class PopulateDBTests(TestCase):
    def test_populate_db_command(self):
        # Run the management command
        call_command('populate_db')


        # Check superhero users
        hero_usernames = [
            'ironman', 'captainamerica', 'spiderman',
            'batman', 'superman', 'wonderwoman'
        ]
        users = User.objects.filter(username__in=hero_usernames)
        self.assertEqual(users.count(), 6)

        # Check profiles
        profiles = UserProfile.objects.all()
        self.assertEqual(profiles.count(), 6)

        # Check teams
        marvel_team = Team.objects.filter(name='Team Marvel').first()
        dc_team = Team.objects.filter(name='Team DC').first()
        self.assertIsNotNone(marvel_team)
        self.assertIsNotNone(dc_team)
        self.assertEqual(marvel_team.members.count(), 3)
        self.assertEqual(dc_team.members.count(), 3)

        # Check activities
        activities = Activity.objects.all()
        self.assertGreaterEqual(activities.count(), 6)

        # Check workouts (should be empty unless populated elsewhere)
        workouts = Workout.objects.all()
        self.assertIsNotNone(workouts)

        # Check leaderboard (should be empty unless populated elsewhere)
        leaderboard = Leaderboard.objects.all()
        self.assertIsNotNone(leaderboard)
