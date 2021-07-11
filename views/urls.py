from . import listentry, shoppinglist
from django.urls import include, path

from . import shoppinglist
from . import listentry

urlpatterns = [
    path('shoppinglist/<int:pk>/', shoppinglist.get.get , name="Shoppinglist Get"),
    path('shoppinglist/<int:pk>/list', listentry.list.list , name="Shoppinglist List"),
]
