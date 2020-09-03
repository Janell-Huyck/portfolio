from django.db import models
from custom_user.models import CustomUser


class GroceryItem(models.Model):
    quantity = models.CharField(max_length=50)
    item_name = models.CharField(max_length=280)
    is_purchased = models.BooleanField(default=False)
    shopper = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.item_name
