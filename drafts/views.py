from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Draft
from .serializers import DraftSerializer
from .permissions import IsAuthor
from django.utils import timezone
from .serializers import DraftSerializer, DraftDetailSerializer
from .models import Draft, Post
from django.utils import timezone

class DraftPublish(generics.UpdateAPIView):
    permission_classes = [IsAuthor]
    serializer_class = DraftSerializer
    queryset = Draft.objects.all()

    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            # 1. Post erstellen
            post = Post.objects.create(
                owner=instance.author,
                title=getattr(instance, "title", ""),
                content=instance.content,
                image=instance.image,
                created_at=timezone.now(),
            )

            instance.status = "published"
            instance.published_at = timezone.now()
            instance.save()

            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class DraftList(generics.ListCreateAPIView):
    serializer_class = DraftSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Draft.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DraftDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor]
    serializer_class = DraftDetailSerializer
    queryset = Draft.objects.all()
