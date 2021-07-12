from . import get, new
from django.urls import path


urlpatterns = [
    path('<int:pk>/', get.get),
    path('new/', new.new),
]
