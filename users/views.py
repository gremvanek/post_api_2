from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.action == "create":
            # Все пользователи могут создавать учетные записи (регистрация)
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ["list", "retrieve"]:
            # Администраторы и авторизованные пользователи могут просматривать пользователей
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "partial_update"]:
            # Администраторы могут обновлять любую учетную запись
            # Пользователи могут обновлять только свою собственную учетную запись
            self.permission_classes = [IsAuthenticated, self.IsOwnerOrAdmin]
        elif self.action == "destroy":
            # Только администраторы могут удалять учетные записи
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = []
        return super().get_permissions()

    class IsOwnerOrAdmin(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            # Администраторы всегда имеют доступ
            if request.user.is_staff:
                return True
            # Пользователь может редактировать только свою собственную учетную запись
            return obj == request.user


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
