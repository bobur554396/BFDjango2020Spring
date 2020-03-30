from django.db import models


class BaseProduct(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    price = models.FloatField()

    def round_price(self):
        return round(self.price, 2)

    def short_name(self):
        raise NotImplementedError()

    class Meta:
        abstract = True


class OnlineProduct(BaseProduct):
    sale = models.CharField()
    status = models.CharField()

    class Meta:
        ordering = ('name',)

    def short_name(self):
        return self.name[:10]


class OfflineProduct(BaseProduct):
    address = models.TextField()

    def short_name(self):
        return self.name[:5]
