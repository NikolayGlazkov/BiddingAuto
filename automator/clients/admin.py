from django.contrib import admin
from .models import Client

class Clientdmin(admin.ModelAdmin):
    list_display = ("cl_inn","full_name","pers_status")
    list_display_links = ("cl_inn",)
    search_fields =("cl_inn","surname",)

    def full_name(self, obj):
        return f"{obj.name} {obj.surname}"

admin.site.register(Client,Clientdmin)
