
from urllib.parse import urlencode

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View

#---------------SIGNUP VIEW------------------
from habits.models import Habit
from tasks.models import Task

from .forms import SignupForm, LoginForm, ProfileForm, UserUpdateForm


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'users/signup.html', {'form' : form})
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('habit_list')

        return render(request, 'users/signup.html', {'form' : form})
        return render(request, 'users/signup.html', {'form': form})

#---------------LOGIN VIEW--------------------

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {"form" : form})
        return render(request, 'users/login.html', {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('habit_list')

        return render(request, 'users/login.html', {"form": form})



#-------------LOGOUT VIEW-----------------

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')

#-----------------PROFILE VIEW--------------------

class ProfileView(View):

    def get(self, request):
        profile_form = ProfileForm(instance=request.user.profile)
        user_form = UserUpdateForm(instance=request.user)
        habits_qs = Habit.objects.filter(user=request.user)
        tasks_qs = Task.objects.filter(user=request.user)
        stats = {
            'total_habits': habits_qs.count(),
            'total_tasks': tasks_qs.count(),
            'completed_tasks': tasks_qs.filter(completed=True).count(),
            'active_habits': habits_qs.order_by('-created_at')[:4],
        }
        return render(request, 'users/profile.html', {
            'profile_form': profile_form,
            'user_form': user_form,
            **stats,
        })

    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')

        habits_qs = Habit.objects.filter(user=request.user)
        tasks_qs = Task.objects.filter(user=request.user)

        return render(request, 'users/profile.html', {
            'profile_form': profile_form,
            'user_form': user_form,
            'total_habits': habits_qs.count(),
            'total_tasks': tasks_qs.count(),
            'completed_tasks': tasks_qs.filter(completed=True).count(),
            'active_habits': habits_qs.order_by('-created_at')[:4],
        })

