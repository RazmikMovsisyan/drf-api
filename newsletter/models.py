from django.db import models
import uuid

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmation_code = models.CharField(max_length=40, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = uuid.uuid4()
        super().save(*args, **kwargs)
