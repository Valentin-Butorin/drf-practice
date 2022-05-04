from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = 'admin'
        password = 'admin'

        User = get_user_model()

        if not User.objects.filter(username=username).exists() and not User.objects.filter(
                is_superuser=True).exists():
            User.objects.create_superuser(
                username=username,
                password=password,
            )
