import telebot
import os
import time

# لو حاطط التوكن في Railway Variables
TOKEN = os.getenv("7852999174:AAG_7TvkWdkdnIfg46dAHkgcpdkvqJWqUXY")

# أو حطه مباشر (لو حابب)
# TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 أهلاً بيك!\n\n"
        "🤖 أنا بوت Python Mentor\n"
        "اسألني أي حاجة عن بايثون 👇"
    )


@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.send_message(
        message.chat.id,
        f"📩 استلمت رسالتك:\n<b>{message.text}</b>\n\n"
        "✅ البوت شغال تمام"
    )


# تشغيل البوت
while True:
    try:
        print("Bot is running...")
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print("Error:", e)
        time.sleep(5)
