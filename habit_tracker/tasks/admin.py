from django.contrib import admin
from .models import Task


#-----------------TASK MODEL REGISTRATION---------------

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "user",
        "priority",
        "due_date",
        "completed",
        "overdue_status",
    )

    list_filter   = ("completed", "priority", "due_date")
    search_fields = ("title", "user__username")
    ordering      = ("-created_at", )

    list_editable = ("completed",)

    def overdue_status(self, obj):
        return "Overdue" if obj.is_overdue() else "Ok"

    overdue_status.short_description = "Status"
