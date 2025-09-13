from rest_framework import serializers
from .models import NewsletterSubscriber

class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email', 'subscribed', 'created_at', 'confirmation_code']
        read_only_fields = ['subscribed', 'created_at', 'confirmation_code']
