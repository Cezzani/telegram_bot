import telebot
from telebot import types
import random



bot = telebot.TeleBot('5446451082:AAGMBnWEzlsm2ECg2oG2EXZifkl1bHv-7hQ', parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "nu privetik, problemi?")

list_morning = ["Действительно доброе утро", "И вам доброе утро",
                "Утро в радость", "Продуктивного и хорошего дня",
                "Доброе утро и хорошего дня","Во Славу Божию"]

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, "Привет, мой создатель." )

    elif message.text == 'privet':
        bot.reply_to( message, "Nu privetik, ja k vashim uslugam" )
    elif message.text == 'hi':
        bot.reply_to( message, "Nu hi, ja k vashim uslugam" )
    elif message.text == "Доброе утро":
        bot.reply_to( message, random.sample(list_morning, 1))
    elif message.text == 'Доброе утро родные':
        bot.reply_to( message, random.sample(list_morning, 1))
    elif message.text == 'как дела?':
        bot.reply_to( message, 'да все хорошо, потихоньку' )
    elif message.text == "Доброе утро мои родные":
        bot.reply_to( message, random.sample( list_morning, 1 ) )
    elif message.text == "Доброе утро родные люди":
        bot.reply_to( message, random.sample( list_morning, 1 ) )

list_photos = ["Ого, фото что надо", "Красиво", "Супер, а это где?","Вау! Красивое фото!"]
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.reply_to(message, random.sample( list_photos, 1 ) )

#@bot.message_handler(content_types=['sticker'])
#def get_user_sticker(message):
#    bot.reply_to(message, 'Вау! Какой красивый смайлик, есть еще?!')

test_list = ["Красивый стикер", "Отличный смайлик, Спасибо", "Смайлик так себе, лучше смени", "Никогла не видел такой смайлик, идеальный"]

@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.reply_to(message,random.sample(test_list, 1))
#print(random.sample(test_list, 1))

bot.infinity_polling()

#bot.message_handler(commands=['start'])
#def start(message):
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
 #   item1 = types.InlineKeyboardButton('Vodka')
  #  item2 = types.InlineKeyboardButton('sigareti')
   # item3 = types.InlineKeyboardButton( 'shmalj' )
    #markup.add(item1, item2, item3)
    #bot.send_message(message.chat.id, 'Nu privetik, {0.first_name}'.format(message.from_user), reply_markup = markup)
