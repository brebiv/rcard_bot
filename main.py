"""
Сделать регистрацию по желанию
"""
from config import token
import glob
import random
from telegram.ext import Updater
from telegram.ext import MessageHandler, CommandHandler

cards = []
num = []
i = 0
for card in glob.glob('cards/*.png'):
    i += 1
    num.append(i)
    cards.append(card)

def randc(bot, update):
    rcard = random.choice(cards)
    rnum = random.choice(num)
    print(rcard)
    bot.send_photo(update.message.chat.id, open(rcard, 'rb'))
    bot.send_message(update.message.chat.id, rnum)

def text_handler(bot, update):
    if update.message.text == "Nice":
        bot.send_message(update.message.chat.id, "Good")

updater = Updater(token)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', randc))
dispatcher.add_handler(MessageHandler(None, text_handler))

if __name__ == '__main__':
    updater.start_polling()
