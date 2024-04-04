from django.contrib import admin
from .models import LotListBank

class LotListBankAdmin(admin.ModelAdmin):
    list_display = ("client","proc_type","end_of_feed","auction_day","lot_place_urls")
    list_display_links = ("client","end_of_feed","auction_day","lot_place_urls")
    search_fields =("client",)

admin.site.register(LotListBank,LotListBankAdmin)