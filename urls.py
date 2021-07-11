from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('sladmin/', admin.site.urls),
    path('api/v<int:version>/', views.api, name='API')
]
