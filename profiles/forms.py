from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=50, initial="Joe")
    last_name = forms.CharField(label="Last name", max_length=50, initial="Doe")
    bio = forms.CharField(label="biography", widget=forms.Textarea)

