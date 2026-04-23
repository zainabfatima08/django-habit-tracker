from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from habits.models import HabitLog
from django.utils.timezone import now, timedelta

User = get_user_model()

@shared_task

def send_weekly_report():

    today    = now().date()
    week_ago = today - timedelta(days=7)

    for user in User.objects.all():

        completed = (
            HabitLog.objects.filter(
                habit__user = user,
                completed   = True,
                date__gte   = week_ago,
            )
            .count()
        )
#-----------------MESSAGE IN EMAIL------------

        message = f"""
        Weekly Habit Report

        You completed {completed} habits this week.
        
        Keep going!
        """
#-----------------EMAIL SEND-------------------

        send_mail(
            "Weekly Report",
            message,
            "no-reply@tracker.com",
            [user.email],
        )
