from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='newsletter-subscribe'),
    path('unsubscribe/<uuid:code>/', views.unsubscribe_with_code, name='newsletter-unsubscribe-with-code'),
    path('unsubscribe_by_email/', views.unsubscribe_with_email, name='newsletter-unsubscribe-with-email'),
]