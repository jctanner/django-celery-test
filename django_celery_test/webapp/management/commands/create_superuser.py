import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create superuser with predefined credentials'

    def handle(self, *args, **kwargs):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')  # Fetch username from environment variable or default to 'admin'
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')  # Fetch email from environment variable or default to 'admin@example.com'
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'adminpassword')  # Fetch password from environment variable or default to 'adminpassword'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
