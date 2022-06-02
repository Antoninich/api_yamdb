from rest_framework import permissions

from users.enums import Roles


class IsUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == Roles.user.name
        )


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == Roles.moderator.name
        )


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return(
            request.user.is_authenticated
            and request.user.role == Roles.admin.name
        )


class AuthorIsOwnerOrReadOnly(permissions.BasePermission):
    edit_methods = ('PUT', 'PATCH', 'DELETE')

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            and request.method in self.edit_methods
        )
