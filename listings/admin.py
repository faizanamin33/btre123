from django.contrib import admin
from .models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publish', 'price', 'list_data', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_publish',)
    list_filter = ('realtor', 'city')
    search_fields = ('title', 'price', 'realtor', 'city', 'state', 'address', 'zipcode')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
