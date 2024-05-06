from rest_framework import permissions # type: ignore


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        print(request.method)
        print(permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS:
            print('true')
            return True
        print('false')
        return obj.id == request.user.id