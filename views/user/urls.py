from . import get
from django.urls import path


urlpatterns = [
    path('<int:pk>/', get.get),
]
