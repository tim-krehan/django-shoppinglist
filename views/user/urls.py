from . import get, new, delete, update
from django.urls import path


urlpatterns = [
    path('new/', new.new),
    path('<int:pk>/', get.get),
    path('<int:pk>/delete/', delete.delete),
    path('<int:pk>/update/', update.update),
]
