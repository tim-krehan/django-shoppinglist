from . import get, delete, update, check, uncheck, api
from django.urls import path


urlpatterns = [
    path('', api.req),
    path('<int:pk>/', get.req),
    path('<int:pk>/delete/', delete.req),
    path('<int:pk>/update/', update.req),
    path('<int:pk>/check/', check.req),
    path('<int:pk>/uncheck/', uncheck.req),
]