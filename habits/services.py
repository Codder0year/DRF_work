import telebot
from django.conf import settings

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

def send_telegram_reminder(user, habit):
    message = f"Напоминание: {habit.action} в {habit.time} в {habit.place}."
    bot.send_message(user.telegram_chat_id, message)