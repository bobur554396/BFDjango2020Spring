from django.core.management.base import BaseCommand
from datetime import datetime
import random

from demo.core.models import Book, Author


class Command(BaseCommand):
    help = 'Delete Book objects from table'

    def add_arguments(self, parser):
        parser.add_argument('book_ids', nargs='+', help='Book ids for delete')

    def handle(self, *args, **kwargs):

        for book_id in kwargs['book_ids']:
            try:
                b = Book.objects.get(id=book_id)
                b.delete()
                self.stdout.write(self.style.SUCCESS(f"Book id: {book_id} was deleted successfully"))
            except Book.DoesNotExist as e:
                self.stdout.write(self.style.ERROR(f"Book id: {book_id} does not exists!"))
