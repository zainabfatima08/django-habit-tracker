from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Profile
#---------------SIGNUP FORM-----------------
class AvatarInput(forms.ClearableFileInput):
    template_name = 'users/widgets/avatar_input.html'


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

    class Meta:
        model  = User
        fields = ('username', 'email', 'password1', 'password2')

#-----------------LOGIN FORM------------------

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

#-------------PROFILE FORM ------------------

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ('first_name', 'last_name', 'username', 'email')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'headline', 'bio')
        widgets = {
            'avatar': AvatarInput(attrs={'accept': 'image/*', 'data-avatar-input': 'true'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a short bio...'}),
            'headline': forms.TextInput(attrs={'placeholder': 'Your headline (e.g. Building better habits daily)'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.help_text = None
