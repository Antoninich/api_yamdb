from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.enums import Roles


class IsUser(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == Roles.user.name
        )


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == Roles.moderator.name
        )


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return(
            request.user.is_authenticated
            and request.user.role == Roles.admin.name
        )


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
