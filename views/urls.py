from . import listentry, shoppinglist
from django.urls import include, path

from . import shoppinglist
from . import listentry

urlpatterns = [
    path('shoppinglist/<int:pk>/', shoppinglist.get.get),
    path('shoppinglist/<int:pk>/list/', listentry.list.list),
    path('listentry/<int:pk>/', listentry.get.get),
]
