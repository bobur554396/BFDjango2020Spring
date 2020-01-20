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
