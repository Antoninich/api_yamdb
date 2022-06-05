from rest_framework.permissions import BasePermission
from users.enums import Roles


class IsMeAndSuperUserAndAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            username_me = view.kwargs.get('username') == 'me'
        except AttributeError:
            username_me = False

        result = (
            request.user.is_authenticated
            and any((
                username_me,
                request.user.role == Roles.admin.name,
                request.user.is_superuser
            ))
        )
        return result
