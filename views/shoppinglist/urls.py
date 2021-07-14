from . import get, list, add, new, update, delete
from django.urls import path


urlpatterns = [
    path('new/', new.req),
    path('<int:pk>/', get.req),
    path('<int:pk>/list/', list.req),
    path('<int:pk>/add/', add.req),
    path('<int:pk>/update/', update.req),
    path('<int:pk>/delete/', delete.req),
]
