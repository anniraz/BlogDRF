from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions

from apps.user.models import *
from apps.user.serializers import *
from apps.user.permissions import IsOwner, IsOwnProfile

class UsersApiView(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
                   
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializer
        return UserSerializerList

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwnProfile(),)
        return (permissions.AllowAny(),)


class UsersAvatarApiView(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin
                         ):

    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(),)
        return (permissions.IsAuthenticated(),)


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
