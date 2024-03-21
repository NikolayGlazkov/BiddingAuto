from django.urls import path
from .views import create_client
app_name = "clients"
urlpatterns = [
    path('add_client/', create_client, name='add_client'),
]
