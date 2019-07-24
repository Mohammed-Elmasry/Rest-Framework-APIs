# this is a file for custom permissions creations

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permission to allow only the owner of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # read permission is allowed to any request
        # so we'll always allow get, head, options requests
        # using the following condition is a short circuit

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

    