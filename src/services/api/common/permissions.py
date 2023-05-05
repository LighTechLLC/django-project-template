from rest_framework.permissions import BasePermission


class DummyPermission(BasePermission):
    def has_permission(self, request, view):
        return True
