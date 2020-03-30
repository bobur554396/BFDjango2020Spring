from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # ordering = ['name',]
        ordering = ('name',)

    def __str__(self):
        # return 'Product id: {}, name: {}'.format(self.id, self.name)
        return f'Product id: {self.id}, name: {self.name}'


class BaseCategory(models.Model):
    name = models.CharField(max_length=200)

    def get_short_name(self):
        return self.name[:4]

    class Meta:
        abstract = True


class SubCategory(BaseCategory):
    test = models.CharField(max_length=200, default='')


class SubCategory2(BaseCategory):
    count = models.IntegerField(default=0)
