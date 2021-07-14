from . import listentry, shoppinglist, user, session
from django.urls import include, path

from .shoppinglist import urls
from .listentry import urls
from .user import urls
from .session import urls
from . import api

urlpatterns = [
    # shoppinglist
    path('shoppinglist/', include(shoppinglist.urls)),
    path('listentry/', include(listentry.urls)),
    path('user/', include(user.urls)),
    path('session/', include(session.urls)),

    # api
    path('', api.req)
]
