from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.team, 'marvel')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='marvel', members=['Test'])
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test', activity='Running', duration=10)
        self.assertEqual(activity.activity, 'Running')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='marvel', points=50)
        self.assertEqual(lb.team, 'marvel')

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(user='Test', workout='Chest Day')
        self.assertEqual(workout.workout, 'Chest Day')
