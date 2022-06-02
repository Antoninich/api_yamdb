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
