from django.contrib import admin
from .models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed", "created_at")
    list_filter = ("subscribed", "created_at")
    search_fields = ("email",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(subscribed=True)
