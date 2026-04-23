from django.shortcuts import render
from django.views import View
from django.db.models import Count
from django.db.models.functions import TruncDay, ExtractWeekDay
from django.utils.timezone import now, timedelta

from habits.models import HabitLog
from tasks.models import Task

class WeeklyReportView(View):

    def get(self, request):

        today    = now().date()
        week_ago = today - timedelta(days = 7)

       #Habit data

        habit_data = (
            HabitLog.objects.filter(
                habit__user = request.user,
                completed   = True,
                date__gte   = week_ago,
            )
            .annotate(day= TruncDay("date"))
            .values("day")
            .annotate(count = Count("id"))
            .order_by("date")
        )
        # Task data

        task_data = (
            Task.objects.filter(
                user          = request.user,
                completed     = True,
                due_date__gte = week_ago,
            )
            .annotate(weekday = ExtractWeekDay("due_date"))
            .values("weekday")
            .annotate(count   = Count("id"))
        )

        context = {
            "habit_data" : list(habit_data),
            "task_data"  : list(task_data),
        }

        return render(request, 'reports/weekly.html', context)