from django.contrib import admin
from .models import Client

class Clientdmin(admin.ModelAdmin):
    list_display = ("cl_inn","name","surname")
    list_display_links = ("surname","name",)
    search_fields =("cl_inn","surname",)

admin.site.register(Client,Clientdmin)
