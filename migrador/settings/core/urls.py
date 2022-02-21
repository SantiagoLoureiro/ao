# Djagno imports
from django.urls import path

# Local imports
from core import views

urlpatterns = [
    path(r'', views.home, name='home'),
]
