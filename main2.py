# habr.com
import telebot, mymodule
token = mymodule.my_token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Приветствую')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай')
bot.polling()