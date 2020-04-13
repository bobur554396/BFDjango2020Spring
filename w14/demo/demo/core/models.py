from django.db import models
from rest_framework import serializers

from demo.auth_.models import MyUser
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


def valid_num_pages(value):
    if not (10 >= value >= 5000):
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

    objects = models.Manager()

    @property
    def price_round(self):
        return round(self.price, 3)

    @classmethod
    def top_ten(cls):
        return cls.objects.all()[:10]

    @staticmethod
    def cmp_books(book1, book2):
        return book1.price > book2.price
