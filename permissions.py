from rest_framework.permissions import BasePermission, SAFE_METHODS


class AllowAnyForSwagger(BasePermission):
    """
    Разрешает доступ к Swagger и OpenAPI без аутентификации.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and (
            request.path.startswith("/swagger/")
            or request.path.startswith("/api/schema/")
        ):
            return True
        return False
