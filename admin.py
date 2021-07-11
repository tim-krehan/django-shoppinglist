from django.contrib import admin

from .models import *

class ListEntryInlineAdmin(admin.TabularInline):
    model = ListEntry
    extra = 1

class ListEntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Shopping List", {'fields': ['shoppinglist']}),
        ("Entry", {'fields': ['name', 'checked']}),
        ("Time Date", {'fields': ['added_at']})
    ]
    list_display = ['name', 'checked']


class ShoppingListAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Shopping List", {'fields': ['name', 'display_name']}),
        ("Permissions", {'fields': ['owner']}),
        ("Time Date", {'fields': ['created_at', 'last_change']})
    ]
    list_display = ['display_name', 'owner', 'last_change']
    inlines = [ListEntryInlineAdmin]

admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(ListEntry, ListEntryAdmin)