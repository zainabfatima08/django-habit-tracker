from django.shortcuts import render
from django.utils.timezone import now
from django.views import View

from habits.models import Habit
from tasks.models import Task


#-----------------HomeView--------------------

class HomeView(View):

    def get(self, request):

        if request.user.is_authenticated:

            habits = Habit.objects.filter(user=request.user)[:5]
            tasks  = Task.objects.filter(user=request.user, completed = False)[:5]

            return render(request, 'core/dashboard.html', {
                'habits' : habits,
                'tasks'  : tasks,
            })

        return render(request, 'core/home.html')
