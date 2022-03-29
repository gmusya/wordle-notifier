import telebot as tg
import threading

bot = tg.TeleBot("487771049:AAGve_n0Q9e0M4mHxvppUh3vWF4S_iHqxgg")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.from_user.id)
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши \"Привет\"")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")    

t1 = threading.Thread(target=bot.polling)
#bot.polling(none_stop=True, interval=3)
t1.start()
print("wow")

from flask import Flask

app = Flask(__name__)


@app.route('/a1')
def hello():
    bot.send_message(356405013, "Hi!")
    return "Hello"


@app.route('/a2')
def hello2():
    bot.send_message(356405013, "Hui!")
    return "Hello2"


if __name__ == "__main__":
    app.run()