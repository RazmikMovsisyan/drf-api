from django.urls import path
from . import views

urlpatterns = [
    path('drafts/', views.DraftList.as_view(), name='draft-list'),
    path('drafts/<int:pk>/', views.DraftDetail.as_view(), name='draft-detail'),
    path('drafts/<int:pk>/publish/', views.DraftPublish.as_view(), name='draft-publish'),
]
