from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializer import UserSerializer

# Create your views here.


class UserViewSet(ModelViewSet):
    """
    Класс для создания представления,
    которое уже имеет систему CRUD
    для класса User
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
