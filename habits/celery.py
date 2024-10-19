from datetime import timezone

import telebot

bot = telebot.TeleBot('TELEGRAM_BOT_TOKEN')

def send_telegram_reminder(user, habit):
    message = f"Напоминание: {habit.action} в {habit.time} в {habit.place}."
    bot.send_message(user.telegram_chat_id, message)

# Celery Task
from celery import shared_task
from .models import Habit

@shared_task
def send_habit_reminders():
    habits = Habit.objects.filter(time__lte=timezone.now().time(), periodicity__gte=1)
    for habit in habits:
        send_telegram_reminder(habit.user, habit)