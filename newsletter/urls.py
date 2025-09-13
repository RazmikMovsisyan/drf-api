from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='newsletter-subscribe'),
    path('unsubscribe/<uuid:code>/', views.unsubscribe, name='newsletter-unsubscribe'),
]