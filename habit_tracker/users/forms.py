from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Profile
#---------------SIGNUP FORM-----------------

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ('username', 'email', 'password1', 'password2')

#-----------------LOGIN FORM------------------

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#-------------PROFILE FORM ------------------

class ProfileForm(forms.ModelForm):

    class Meta:
        model  = Profile
        fields = ("dark_mode",)
