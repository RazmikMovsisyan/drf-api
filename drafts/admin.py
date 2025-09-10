from django.contrib import admin
from .models import Draft

@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = ['author', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    search_fields = ['author__username', 'content']
