from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create 5 demo users with password Admin@1234'

    def handle(self, *args, **options):
        demo_users = [
            {'username': 'demo_user1', 'email': 'demo1@example.com'},
            {'username': 'demo_user2', 'email': 'demo2@example.com'},
            {'username': 'demo_user3', 'email': 'demo3@example.com'},
            {'username': 'demo_user4', 'email': 'demo4@example.com'},
            {'username': 'demo_user5', 'email': 'demo5@example.com'},
        ]

        password = 'Admin@1234'

        for user_data in demo_users:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={'email': user_data['email']},
            )
            if created:
                user.set_password(password)
                user.save()
                self.stdout.write(self.style.SUCCESS(
                    f"Created user: {user_data['username']}"
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f"User already exists: {user_data['username']}"
                ))

        self.stdout.write(self.style.SUCCESS('\nAll 5 demo users ready!'))
        self.stdout.write(f'Password for all users: {password}')
