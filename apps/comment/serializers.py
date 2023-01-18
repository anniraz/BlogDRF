from rest_framework import serializers

from apps.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('id', 'user', 'create_at',)




