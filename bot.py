import config
import telebot
import random

TOKEN = config.token
bot = telebot.TeleBot(TOKEN)

quotes = [
    "«Каждый день — новая возможность стать лучше, чем вчера.»",
    "«Не бойся делать ошибки. Бойся не попробовать.»",
    "«Успех — это сумма маленьких усилий, повторяемых изо дня в день.»",
    "«Твое будущее создаётся тем, что ты делаешь сегодня, а не завтра.»",
    "«Сила не в том, чтобы никогда не падать, а в том, чтобы каждый раз подниматься.»",
    "«Мечты не работают, если ты не работаешь.»",
    "«Не жди подходящего момента — создай его сам.»",
    "«Трудности — это просто ступени к вершине успеха.»",
    "«Верь в себя, и весь мир поверит в тебя.»",
    "«Самый длинный путь начинается с первого шага.»"
]

@bot.message_handler(commands=['start'])
def greetings(message):
    bot.reply_to(message,"Привет я Frija's Bot, напиши /info чтобы узнать какие у меня есть команды.")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message,"Привет я Frija's Bot пока что я могу давать тебе интересные, мотивирующие цитаты.")


@bot.message_handler(commands=['quote'])
def send_message(message):
    rand_quote = random.choice(quotes)
    bot.reply_to(message,rand_quote)
    

bot.infinity_polling()