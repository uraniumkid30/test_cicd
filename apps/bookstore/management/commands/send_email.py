from django.core.management.base import BaseCommand
from apps.user.models import User


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument("my_email", type=str)

    def handle(self, *args, **kwargs):
        # list users
        all_users = User.objects.all()
        for user in all_users:
            print(f"Sending email to  {user.email}")
        # email = kwargs.get("my_email")
        self.stdout.write("Sent All Emails")
