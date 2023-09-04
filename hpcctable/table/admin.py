from django.contrib import admin
from .models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'parent_group')
    list_filter = ('parent_group',)
    search_fields = ('name', 'year')
    ordering = ('name',)

admin.site.register(Group, GroupAdmin)
