import telebot

TOKEN = "7852999174:AAG_7TvkWdkdnIfg46dAHkgcpdkvqJWqUXY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👋 أهلاً بيك!\n\n"
        "🤖 أنا بوت تعليم بايثون من الصفر\n\n"
        "✍️ اسألني أي حاجة عن Python\n"
        "مثال:\n"
        "- يعني ايه variable\n"
        "- اكتبلي كود بسيط\n"
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text.lower()

    if "variable" in text or "متغير" in text:
        bot.reply_to(
            message,
            "📌 المتغير في بايثون:\n"
            "x = 5\n"
            "name = 'Ali'\n\n"
            "بيستخدم لتخزين البيانات."
        )
    elif "loop" in text or "for" in text:
        bot.reply_to(
            message,
            "🔁 مثال على for loop:\n\n"
            "for i in range(5):\n"
            "    print(i)"
        )
    else:
        bot.reply_to(
            message,
            "🤔 سؤالك حلو!\n"
            "اسألني عن:\n"
            "- variables\n"
            "- loops\n"
            "- functions\n"
            "- examples"
        )

print("Bot is running...")
bot.infinity_polling()
