from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)


class IsOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)

