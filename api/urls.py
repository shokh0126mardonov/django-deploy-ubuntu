from django.urls import path

from .views import TestApi

urlpatterns = [
    path('api/test/',TestApi)
]