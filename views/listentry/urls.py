from . import get, delete, update, check, uncheck
from django.urls import path


urlpatterns = [
    path('<int:pk>/', get.get),
    path('<int:pk>/delete/', delete.delete),
    path('<int:pk>/update/', update.update),
    path('<int:pk>/check/', check.check),
    path('<int:pk>/uncheck/', uncheck.uncheck),
]