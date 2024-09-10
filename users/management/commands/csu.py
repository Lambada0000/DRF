from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@gmail.com")
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password("90539053")
        user.save()