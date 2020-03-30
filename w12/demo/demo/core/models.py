from django.db import models
from rest_framework import serializers

from demo.utils.validators import validate_file_size, validate_extension


class Publisher(models.Model):
    """Publisher class"""
    MALE = 1
    FEMALE = 2
    GENDER = (
        (MALE, 'male'),
        (FEMALE, 'female'),
    )
    name = models.CharField(max_length=300, unique=True)
    city = models.CharField(max_length=300)
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=MALE)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'
        # unique_together = ('name', 'city')
        # ordering = ('name',)
        # db_table = 'publishers_table'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        pass


class Author(models.Model):
    photo = models.ImageField(upload_to='author_photos',
                              validators=[validate_file_size,
                                          validate_extension],
                              null=True, blank=True)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)

    # creator = models.ForeignKey(MainUser)

    def __str__(self):
        return f'ID: {self.id}, name: {self.name}'

    def set_new_rating(self, value):
        self.rating = value
        self.save()

    # @property
    def books_count(self):
        pass
        # return self.books.count()


# print(a.books_count)


# class PublishedBook(models.Manager):
#     def get_queryset(self):
#         return self.filter(is_published=True)
#
#     def filter_by_name(self, name_pattern):
#         return self.filter(name__contains=name_pattern)
#
#
# class NotPublishedBook(models.Manager):
#     def get_queryset(self):
#         return self.filter(is_published=False)


def valid_num_pages(value):
    if not(10 >= value >= 5000):
        raise serializers.ValidationError('invalid num of pages')


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    num_pages = models.IntegerField(default=0,
                                    validators=[valid_num_pages])
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='books')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  related_name='books')

    objects = models.Manager()
    # published_books = PublishedBook()
    # not_published_books = NotPublishedBook()

    @property
    def price_round(self):
        return round(self.price, 3)

    @classmethod
    def top_ten(cls):
        return cls.objects.all()[:10]

    @staticmethod
    def cmp_books(book1, book2):
        return book1.price > book2.price



# b1 = Book()
# print(b1.price_round)
#
# b2 = Book()
#
# ret = Book.cmp_books(b1, b2)


class Tag(models.Model):
    name = models.CharField(max_length=200)


class BookTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            related_name='books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='tags')

# t = Tag()
# t.books.all()
#
# b = Book()
# for book_tag in b.tags.all():
#     print(book_tag.tag)
#
