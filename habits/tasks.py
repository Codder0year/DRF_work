from celery import shared_task
from django.utils import timezone
from .models import Habit
from .services import send_telegram_reminder

@shared_task
def send_habit_reminders():
    habits = Habit.objects.filter(time__lte=timezone.now().time(), periodicity__gte=1)
    for habit in habits:
        send_telegram_reminder(habit.user, habit)