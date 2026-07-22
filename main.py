import os
import telebot
import random

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

answers = [
    "Интересный вопрос! Я думаю об этом.",
    "Хм, надо над этим поразмышлять...",
    "Я всего лишь бот, но звучит круто!",
    "Расскажи подробнее, мне очень интересно.",
    "Понял тебя! А что было дальше?",
    "Круто! Полностью с тобой согласен."
]

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    reply_text = random.choice(answers)
    bot.reply_to(message, reply_text)

print("Бот запущен...")
bot.infinity_polling()
