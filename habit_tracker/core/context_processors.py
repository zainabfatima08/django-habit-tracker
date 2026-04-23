from habits.models import Habit
from tasks.models import Task

#-------------DASHBOARD STATS-----------

def dashboard_stats(request):

    if not request.user.is_authenticated:
        return {}

    return {
        "total_habits" : Habit.objects.filter(user=request.user).count(),
        "pending_tasks": Task.objects.filter(user=request.user, completed=False).count(),
    }

# ------------PROFILE THEME------------------
def theme(request):

    if not request.user.is_authenticated:
        return {}

    return {
        "dark_mode": request.user.profile.dark_mode
    }