from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Insert test users
        User.objects.bulk_create([
            User(name='Iron Man', email='ironman@marvel.com', team='marvel'),
            User(name='Captain America', email='cap@marvel.com', team='marvel'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='dc'),
            User(name='Batman', email='batman@dc.com', team='dc'),
        ])

        # Insert teams
        Team.objects.bulk_create([
            Team(name='marvel', members=['Iron Man', 'Captain America']),
            Team(name='dc', members=['Wonder Woman', 'Batman']),
        ])

        # Insert activities
        Activity.objects.bulk_create([
            Activity(user='Iron Man', activity='Running', duration=30),
            Activity(user='Wonder Woman', activity='Cycling', duration=45),
        ])

        # Insert leaderboard
        Leaderboard.objects.bulk_create([
            Leaderboard(team='marvel', points=100),
            Leaderboard(team='dc', points=90),
        ])

        # Insert workouts
        Workout.objects.bulk_create([
            Workout(user='Iron Man', workout='Chest Day'),
            Workout(user='Batman', workout='Leg Day'),
        ])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
