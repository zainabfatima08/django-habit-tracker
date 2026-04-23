from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View

from .models import Task
from .forms import TaskForm

#-----------------LIST VIEW-----------------

class TaskListView(View):

    def get(self, request):
        tasks = Task.objects.filter(user=request.user).order_by("created_at")
        form = TaskForm()

        return render(request, "tasks/list.html", {
            "tasks": tasks,
            "form" : form,
        })

#---------------------CREATE VIEW----------------

class TaskCreateView(View):
    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            task      = form.save(commit=False)
            task.user = request.user
            task.save()

        return redirect("task_list")

#-------------------TOGGLE VIEW--------------------

class TaskToggleView(View):

    def post(self, request, pk):
        task = get_object_or_404(Task, pk =pk , user = request.user)

        task.completed = not task.completed
        task.save()

        if request.headers.get("HX-Request"):
            return HttpResponse(
                "Done" if task.completed else "Pending"
            )

        return redirect("task_list")

#---------------- DELETE VIEW-------------------

class TaskDeleteView(View):

    def post(self, request, pk):
        task = get_object_or_404(Task , pk =pk , user = request.user)
        task.delete()

        return redirect("task_list")

