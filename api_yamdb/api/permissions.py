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
        return (
            request.user.is_superuser
            or request.user.is_authenticated
            and request.user.role == Roles.admin.name
        )


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsPostAndAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' and request.user.is_authenticated


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReadOnlyOrAuthorModeratorAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or obj.author == request.user
            or not request.user.is_anonymous
            and request.user.role in [Roles.moderator.name, Roles.admin.name]
        )
