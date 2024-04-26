from django.contrib import admin

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'created_at', 'updated_at']
    list_filter = ['created_at']


admin.site.register(Team, TeamAdmin)
