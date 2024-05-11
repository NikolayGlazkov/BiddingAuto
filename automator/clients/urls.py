from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("login/", login, name="login"),
    path("contact/", contact, name="contact"),
    path("add_client/", add_client, name="add_client"),
    path("clients_list/", clients_list, name="clients_list"),
    path('show_client/<str:cl_inn>/', show_client, name='show_client'),
    path('find_client/', find_client, name='find_client'),
    path("run-script/", run_script_view, name="run_script"),
    path("edit_client/<str:cl_inn>",edit_client,name = "edit_client"),
    path('delete_client/<str:cl_inn>/', delete_client, name='delete_client'),
    
    path("add_lot/<int:cl_inn>", add_lot, name="add_lot"),
    path("lot_list/", lot_list, name="lot_list"),
    path("edit_lot/<int:id>/",edit_lot,name="edit_lot"),
    path('events/', lot_events, name='lot-events'),
]
