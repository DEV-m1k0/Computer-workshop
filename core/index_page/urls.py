from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="index"),
    path("reg/", include("reg.urls")),
]
