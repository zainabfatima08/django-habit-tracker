from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import SignupForm, LoginForm, ProfileForm
from django.contrib.auth import login, logout, authenticate

#---------------SIGNUP VIEW------------------

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'users/signup.html', {'form' : form})

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('habit_list')

        return render(request, 'users/signup.html', {'form' : form})

#---------------LOGIN VIEW--------------------

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {"form" : form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('habit_list')

        return render(request, 'users/login.html', {"form" : form})

#-------------LOGOUT VIEW-----------------

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')

#-----------------PROFILE VIEW--------------------

class ProfileView(View):

    def get(self, request):
        form = ProfileForm(instance=request.user.profile)
        return render(request, 'users/profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect("profile")

        return render(request, 'users/profile.html', {'form': form})

