from django.views.generic import FormView
from .forms import RegUserForm

# Create your views here.


class UserRegViewSet(FormView):
    template_name = "reg.html"
    form_class = RegUserForm
