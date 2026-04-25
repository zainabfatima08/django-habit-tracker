from django.db import models
from django.conf import settings
from django.utils.timezone import now

User = settings.AUTH_USER_MODEL

class Task(models.Model):

    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    user       = models.ForeignKey(User, on_delete = models.CASCADE)
    title      = models.CharField(max_length=255)
    due_date   = models.DateField()
    priority   = models.CharField(max_length=1, choices = PRIORITY_CHOICES)
    completed  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)

    def is_overdue(self):
        return not self.completed and self.due_date < now().date()

    def days_left(self):
        return (self.due_date - now().date()).days

    def __str__(self):
        return self.title


