from . import get
from . import list
from django.urls import path


urlpatterns = [
    path('<int:pk>/', get.get),
    path('<int:pk>/list/', list.list),
]
