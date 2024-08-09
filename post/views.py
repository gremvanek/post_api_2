from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.exceptions import PermissionDenied


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAuthenticated, IsAdminUser | self.IsOwner]
        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, IsAdminUser | self.IsOwner]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        if (
            not self.request.user.is_superuser
            and serializer.instance.author != self.request.user
        ):
            raise PermissionDenied("You do not have permission to edit this post.")
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if not self.request.user.is_superuser and instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this post.")
        super().perform_destroy(instance)

    class IsOwner(BasePermission):
        def has_object_permission(self, request, view, obj):
            return obj.author == request.user


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAuthenticated, IsAdminUser | self.IsOwner]
        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, IsAdminUser | self.IsOwner]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        if (
            not self.request.user.is_superuser
            and serializer.instance.author != self.request.user
        ):
            raise PermissionDenied("You do not have permission to edit this comment.")
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if not self.request.user.is_superuser and instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this comment.")
        super().perform_destroy(instance)

    class IsOwner(BasePermission):
        def has_object_permission(self, request, view, obj):
            return obj.author == request.user
