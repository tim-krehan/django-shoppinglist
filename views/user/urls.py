from . import get, new, delete, update
from django.urls import path


urlpatterns = [
    path('new/', new.req),
    path('<int:pk>/', get.req),
    path('<int:pk>/delete/', delete.req),
    path('<int:pk>/update/', update.req),
]
