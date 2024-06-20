from django.urls import path
from . import views

urlpatterns = [path("", views.UserRegViewSet.as_view(), name="reg")]
