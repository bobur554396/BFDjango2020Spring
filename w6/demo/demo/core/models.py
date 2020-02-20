from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'
        # ordering = ('name',)


class Author(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    # creator = models.ForeignKey(MainUser)

    def __str__(self):
        return self.name

    def set_new_rating(self, value):
        self.rating = value
        self.save()


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    num_pages = models.IntegerField(default=0)
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='booksc')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.CASCADE,
                                  related_name='books')
