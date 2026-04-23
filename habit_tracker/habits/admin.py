from django.contrib import admin
from .models import Habit, HabitLog

#--------------HABITLOGINLINE-------------------

class HabitLogInline(admin.TabularInline):
    model           = HabitLog
    extra           = 0
    fields          = ("date", "completed")
    readonly_fields = ("date",)
    can_delete      = False
    ordering        = ("-date",)

#-----------HABIT MODEL REGISTRATION--------------

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):

    list_display =(
        "id",
        "title",
        "user",
        "created_at",
        "current_streak_display",

    )

    list_filter   = ("created_at", "user")
    search_fields = ("title", "user__username")
    ordering      = ("created_at", )

    Inlines = [HabitLogInline]

    def current_streak_display(self, obj):
        return obj.current_streak()

    current_streak_display.short_description = "Streak"

#--------------- HABITLOG MODEL ----------------

@admin.register(HabitLog)
class HabitLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "habit",
        "date",
        "completed",
    )

    list_filter   = ("completed", "date", "habit")
    search_fields = ("habit__title","habit__user__username")
    ordering      = ("-date",)

    list_editable = ("completed", )

