from django.shortcuts import render
from django.utils.timezone import now
from django.views import View

from habits.models import Habit
from tasks.models import Task


#-----------------HomeView--------------------

class HomeView(View):

    def get(self, request):

        if request.user.is_authenticated:

            habits_qs = Habit.objects.filter(user=request.user)
            tasks_qs = Task.objects.filter(user=request.user, completed=False)

            return render(request, 'core/dashboard.html', {
                'habits': habits_qs[:5],
                'tasks': tasks_qs[:5],
                'total_habits': habits_qs.count(),
                'pending_tasks': tasks_qs.count(),
            })

        return render(request, 'core/home.html')
