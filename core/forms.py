from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#signup form is created, length is defined and compulsory field
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]