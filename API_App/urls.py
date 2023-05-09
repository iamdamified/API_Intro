from django.urls import path
from .views import api_home_page

urlpatterns = [
    path("", api_home_page, name="api-home-page")
]