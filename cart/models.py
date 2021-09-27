from django.db import models


class Cart(models.Model):
    product_id = models.IntegerField()
