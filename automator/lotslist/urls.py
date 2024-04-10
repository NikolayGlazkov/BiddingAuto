from django.urls import path, re_path
from .views import *

urlpatterns = [
    
    path("add_lot/", add_lot, name="add_lot"),
     
]
