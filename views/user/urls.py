from . import get, new, delete, update, api
from django.urls import path


urlpatterns = [
    path('', api.req),
    path('new/', new.req),
    path('<int:pk>/', get.req),
    path('<int:pk>/delete/', delete.req),
    path('<int:pk>/update/', update.req),
]
