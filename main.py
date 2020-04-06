import telebot
from telebot import types
from secret_stuff import token

bot = telebot.TeleBot(token)
users_id = []


def id_storage(some_id):
    if any(k == some_id for k in users_id) == False:
        users_id.append(some_id)
    else:
        pass
    print(users_id)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    id_storage(message.chat.id)
    send_mess = f"<b>Howdy ,{message.from_user.first_name}, how are you doing?</b>\n Here is a link to channel:\n@chee_tam"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(commands=['text'])
def not_anonymous(message):
    send_mess = message.from_user
    bot.send_message(message.chat.id, send_mess)
    print(message.from_user)


@bot.message_handler(commands=['mail'])
def mailing(message):

    if message.from_user.id != 336972408:
        pass
    else:
        for user in users_id:
            bot.send_message(user, "Здарова тварына")


@bot.message_handler(func=lambda m: True)
def repeater(message):
    # send_mess = message.text
    photo = open('C:/Users/Никита/Downloads/putin.jpg', 'rb')
    caption = message.from_user.first_name + ", думаю как тебя наказать, пешка навального"

    bot.send_message(message.chat.id, caption)
    bot.send_photo(message.chat.id, photo)
    print(message.text)


#@bot.message_handler(content_types=['text'])
#def some_func(message):

bot.polling(none_stop=True)
