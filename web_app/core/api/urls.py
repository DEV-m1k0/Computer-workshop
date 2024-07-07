from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Создаем объект для регистарции маршрутов
router = DefaultRouter()
# Регистрируем маршруты для отображения всех пользователей системы
router.register("users", UserViewSet)

urlpatterns = [path("", include(router.urls))]
