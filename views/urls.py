from . import listentry, shoppinglist
from django.urls import include, path

from . import shoppinglist
from . import listentry
from . import user

urlpatterns = [
    # shoppinglist
    path('shoppinglist/<int:pk>/', shoppinglist.get.get),
    path('shoppinglist/<int:pk>/list/', listentry.list.list),

    # shoppinglist entries
    path('listentry/<int:pk>/', listentry.get.get),

    # user
    path('user/<int:pk>/', user.get.get),
]
