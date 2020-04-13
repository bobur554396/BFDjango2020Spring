from django.core.management.base import BaseCommand
from datetime import datetime
import random

from demo.core.models import Book, Author


def create_authors(num=3):
    authors = [Author(name=f'author {i}',
                      email=f'author {i}@gmail.com', )
               for i in range(num)]

    Author.objects.bulk_create(authors)


class Command(BaseCommand):
    help = 'Create fake date for Book table'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of books for creation')

        parser.add_argument('-p', '--prefix', type=str, help='Prefix string for new books')

        parser.add_argument('-e', '--exp', action='store_true', help='Create Book with expensive price')

    def handle(self, *args, **kwargs):
        # Book.objects.all().delete()

        total = kwargs['total']
        prefix = kwargs.get('prefix')
        expensive = kwargs.get('exp')

        if not prefix:
            prefix = 'AA'

        create_authors(total)

        # # self.stdout.write()
        # for i in range(total):
        #     if expensive:
        #         b = Book.objects.create(name=f'{prefix}_book {i}',
        #                                 price=100000,
        #                                 author_id=1)
        #     else:
        #         b = Book.objects.create(name=f'{prefix}_book {i}',
        #                                 price=random.randint(500, 2000),
        #                                 author_id=1)
        #     self.stdout.write(f'Book {b.id} was created')
