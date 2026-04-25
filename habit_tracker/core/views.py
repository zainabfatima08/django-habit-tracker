from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.views import View

from habits.models import Habit, HabitLog
from tasks.models import Task


#-----------------HomeView--------------------

class HomeView(View):

    def get(self, request):

        if request.user.is_authenticated:
            habits_qs        = Habit.objects.filter(user=request.user)
            tasks_qs         = Task.objects.filter(user=request.user)
            pending_tasks_qs = tasks_qs.filter(completed=False)

            today = now().date()
            week_start = today - timedelta(days=6)

            completed_habits_week = HabitLog.objects.filter(
                habit__user = request.user,
                completed   = True,
                date__gte   = week_start,
            ).count()

            completed_tasks = tasks_qs.filter(completed=True).count()
            total_tasks = tasks_qs.count()

            completion_rate = int((completed_tasks / total_tasks) * 100) if total_tasks else 0

            if completion_rate >= 75:
                productivity_message = 'Excellent momentum. Keep this streak alive.'
            elif completion_rate >= 45:
                productivity_message = 'Good progress. Complete a few more tasks today.'
            else:
                productivity_message = 'Start small today—finish 1 task to build momentum.'

            badges = []
            if completed_habits_week >= 5:
                badges.append('Consistency Star')
            if completion_rate >= 70:
                badges.append('Focus Finisher')
            if pending_tasks_qs.count() == 0 and total_tasks > 0:
                badges.append('Inbox Zero')
            return render(request, 'core/dashboard.html', {

                'habits': habits_qs[:5],
                'tasks': pending_tasks_qs[:5],
                'total_habits': habits_qs.count(),
                'pending_tasks': pending_tasks_qs.count(),
                'completed_tasks': completed_tasks,
                'completion_rate': completion_rate,
                'completed_habits_week': completed_habits_week,
                'productivity_message': productivity_message,
                'badges': badges,
            })

        return render(request, 'core/home.html')
