from rest_framework import generics, permissions
from .models import Draft
from .serializers import DraftSerializer, DraftDetailSerializer
from .permissions import IsAuthor

class DraftList(generics.ListCreateAPIView):
    serializer_class = DraftSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Draft.objects.filter(author=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class DraftDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor]  # Geändert
    serializer_class = DraftDetailSerializer
    queryset = Draft.objects.all()

class DraftPublish(generics.UpdateAPIView):
    permission_classes = [IsAuthor]  # Geändert
    serializer_class = DraftSerializer
    queryset = Draft.objects.all()
    
    def perform_update(self, serializer):
        instance = self.get_object()
        instance.publish()
