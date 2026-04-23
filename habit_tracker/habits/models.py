from django.db import models
from django.conf import settings
from django.utils.timezone import now

User = settings.AUTH_USER_MODEL

#-------------HABIT MODEL-----------------

class Habit(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    title      = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def current_streak(self):
        logs   = self.logs.order_by("-date")
        streak = 0
        today  = now().date()

        for log in logs:
            if log.date == today:
                streak  += 1
                today   = today.replace(day=today.day - 1)
            else:
                break
        return streak

#--------------HABITLOG MODEL-----------------

class HabitLog(models.Model):
    habit     = models.ForeignKey(Habit, related_name = "logs", on_delete=models.CASCADE )
    date      = models.DateField(default = now)
    completed = models.BooleanField(default = False)

    class Meta:
        unique_together = ("habit", "date")

