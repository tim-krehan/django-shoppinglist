from . import listentry, shoppinglist
from django.urls import include, path

from . import shoppinglist
from . import listentry
from . import user

urlpatterns = [
    path('shoppinglist/<int:pk>/', shoppinglist.get.get),
    path('shoppinglist/<int:pk>/list/', listentry.list.list),
    path('listentry/<int:pk>/', listentry.get.get),
    path('user/<int:pk>/', user.get.get),
]
