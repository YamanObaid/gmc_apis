from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class Command(BaseCommand):
    help = 'Generate JWT token for a user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            user = User.objects.get(username=username)
            refresh = RefreshToken.for_user(user)
            self.stdout.write(self.style.SUCCESS(f'Access Token: {refresh.access_token}'))
            self.stdout.write(self.style.SUCCESS(f'Refresh Token: {refresh}'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User "{username}" does not exist'))
