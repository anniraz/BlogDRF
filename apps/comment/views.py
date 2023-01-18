from rest_framework import viewsets,permissions

from apps.comment.serializers import CommentSerializer
from apps.comment.models import Comment
from apps.user.permissions import IsOwner


class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)