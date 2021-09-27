from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.ImageField(upload_to='upload/images')

    def __str__(self) -> str:
        return self.title
