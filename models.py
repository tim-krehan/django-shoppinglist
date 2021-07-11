from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

class ShoppingList(models.Model):
    name = models.CharField(max_length=256)
    display_name = models.CharField(max_length=256, null=True)
    owner = models.ForeignKey(User,on_delete=CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    last_change = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.display_name


class ListEntry(models.Model):
    shoppinglist = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    checked = models.BooleanField(default=False)
    added_at = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name