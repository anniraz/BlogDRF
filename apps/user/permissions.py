from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    '''
    permission for owner verification
    '''
    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)


class IsOwnProfile(permissions.BasePermission):
    '''
    permission for own profile
    '''
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)

