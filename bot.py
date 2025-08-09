import config
import telebot

TOKEN = config.token
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def greetings(message):
    bot.reply_to(message,"Привет я Frija's Bot")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message,"""Привет я Frija's Bot пока что я 
                 только умею повторять за тобой сообщения.""")


@bot.message_handler()
def send_message(message):
    bot.reply_to(message,message.text)

bot.infinity_polling()