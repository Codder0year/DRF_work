from rest_framework import permissions

class IsModer(permissions.BasePermission):
    """Проверка на модерацию."""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()

class  IsOwner(permissions.BasePermission):
    """Проверка является ли пользователь владельцем объекта."""

    def has_object_permission(self, request, view, obj):
          if obj.owner == request.user:
              return True
          return False
