from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth import get_user_model
from .models import UserProfile, Team, Activity

User = get_user_model()


class PopulateDBTests(TestCase):
    def test_populate_db_command(self):
        # Run the management command
        call_command('populate_db')

        # Check users
        users = User.objects.filter(username__in=['user1', 'user2', 'user3'])
        self.assertEqual(users.count(), 3)

        # Check profiles
        profiles = UserProfile.objects.all()
        self.assertEqual(profiles.count(), 3)

        # Check team
        team = Team.objects.filter(name='Team Alpha').first()
        self.assertIsNotNone(team)
        self.assertEqual(team.members.count(), 3)

        # Check activities
        activities = Activity.objects.all()
        self.assertGreaterEqual(activities.count(), 3)
