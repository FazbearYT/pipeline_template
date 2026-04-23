import telebot
import sqlite3
import os

# токен бота не в env


BOT_TOKEN = "5240018753:AAH-9-YXLggScFMGHiIYB0q7zyoS2Fuk85c"


# BOT_TOKEN = os.getenv("MY_BOT_TOKEN")



bot = telebot.TeleBot(BOT_TOKEN)

# подключаемся к базе
conn = sqlite3.connect('logs.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages (user_id INTEGER, text TEXT)")
conn.commit()


def save_to_db(user_id, text):
    # плохой вариант, может быть инъекция


    query = f"INSERT INTO messages (user_id, text) VALUES ({user_id}, '{text}')"
    cursor.execute(query)


    # правильный вариант


    # query = "INSERT INTO messages (user_id, text) VALUES (?, ?)"
    # cursor.execute(query, (user_id, text))

    conn.commit()


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я зеркало. Напиши мне что-нибудь.")


@bot.message_handler(content_types=['text'])
def mirror(message):
    save_to_db(message.from_user.id, message.text)
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    print("Запущено!")
    bot.infinity_polling()