from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        current_dt = timezone.now()
        self.stdout.write(f"current time {current_dt}")