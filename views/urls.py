from django.urls import path

from . import api

urlpatterns = [
    path('shoppinglist/', api.shoppinglist, name="ShoppingList"),
    path('listentry/', api.listentry, name="List Entry")
]
