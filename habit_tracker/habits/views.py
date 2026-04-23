from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.timezone import now
from django.http import HttpResponse

from .models import Habit, HabitLog

#-------------HBAITLISTVIEW--------------------

class HabitListView(View):

    def get(self, request):
        habits = Habit.objects.filter(user=request.user).order_by("-created_at")
        return render(request, "habits/list.html", {
            "habits" : habits
        })

#------------------CREATE VIEW---------------

class HabitCreateView(View):
    def post(self, request):
        title = request.POST.get("title")

        if title:
            Habit.objects.create(
                user = request.user,
                title = title
            )

        return redirect("habit_list")

#-------------------TOGGLE VIEW -------------------

class ToggleHabitView(View):

    def post(self, request, pk):

        habit = get_object_or_404(Habit, pk=pk, user=request.user)

        log, created = HabitLog.objects.get_or_create(
            habit    =habit,
            date     =now().date(),
            defaults ={"completed": False}
        )

        log.completed = not log.completed
        log.save()

        # HTMX response
        if request.headers.get("HX-Request") == "true":
            return HttpResponse(
                f"<span>{'Done' if log.completed else 'Not Done'}</span>"
            )

        return redirect("habit_list")

class HabitDetailView(View):
    def get(self, request, pk):
        habit = get_object_or_404(Habit, pk = pk, user = request.user)

        logs = habit.logs.order_by("-date")

        return render(request, "habits/detail.html",{
            "habit"  : habit,
            "logs"   : logs,
            "streak" : habit.current_streak()
        })

