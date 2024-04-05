from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("add_lot/", add_lot, name="add_lot"),
    # path("about/", about, name="about"),
    # path("clients_list/", clients_list, name="clients_list"),
    # path("add_client/", add_client, name="add_client"),
    # path("contact/", contact, name="contact"),
    # path("login/", login, name="login"),
    # path("show_client/",show_client,name="show_client"),
    # path('run-script/', run_script_view, name='run_script'),    
]
