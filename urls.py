from django.contrib import admin
from django.urls import include ,path

from . import views
from .views import urls

urlpatterns = [
    path('sladmin/', admin.site.urls),
    path('api/v<int:version>/', include(views.urls))
]
