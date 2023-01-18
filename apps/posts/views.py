from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import viewsets,permissions
from rest_framework.response import Response

from apps.posts.serializers import PostSerializer,PostImageSerializer,PostLikeSerializers
from apps.posts.models import Post,PostImage,PostsLike
from apps.posts.permissions import IsPostOwner
from apps.user.permissions import IsOwner

User=get_user_model()



class PostApiViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)




class PostImageApiViewSet(viewsets.ModelViewSet):

    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsPostOwner(), )
        else:
            return (permissions.IsAuthenticated(),)  


    def create(self, request, *args, **kwargs):
        post = request.data['post']
        owner=Post.objects.get(id=post).user
        user = request.user
        if user==owner:
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You cannot add an image, you are not the owner of this post"})



class PostLikeApiView(viewsets.ModelViewSet):

    queryset=PostsLike.objects.all()
    serializer_class=PostLikeSerializers
    

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)


    def create(self, request, *args, **kwargs):

        post = request.data['post']
        user=request.user       
        if  PostsLike.objects.filter(post_id=post,user=user):
            return Response({"error":"you can't like twice"})
        return super().create(request,*args, **kwargs)



    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    