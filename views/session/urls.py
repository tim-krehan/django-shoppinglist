from . import api, login
from django.urls import path


urlpatterns = [
    path('', api.req),
    path('login/', login.req)
]
