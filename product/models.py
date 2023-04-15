from django.db import models


class Product(models.Model):
    """Product Model Definition"""
    name = models.CharField(max_length=100)
    detail = models.TextField(blank=True, default="")
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    shop = models.ForeignKey(
        "shop.Shop", on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return f"{self.name}"
