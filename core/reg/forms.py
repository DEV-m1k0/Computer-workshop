from django.contrib.auth import forms
from django.contrib.auth.models import User


class RegUserForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        fields = ["username", "email", "password1", "password2"]
