from django.core.management.base import BaseCommand
from apps.bookstore.models import Book


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        my_books = Book.objects.all()
        self.stdout.write(f"We currently found {len(my_books)} books")