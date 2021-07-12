from . import listentry, shoppinglist, user
from django.urls import include, path

from .shoppinglist import urls
from .listentry import urls
from .user import urls

urlpatterns = [
    # shoppinglist
    path('shoppinglist/', include(shoppinglist.urls)),

    # shoppinglist entries
    path('listentry/', include(listentry.urls)),

    # user
    path('user/', include(user.urls)),
]
