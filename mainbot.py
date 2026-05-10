import telebot
import config
from telebot import types   


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Вот список команд:\n/start - начать общение\n/hello - поздороваться\n/bye - попрощаться\n/help - показать эту помощь")

@bot.message_handler(func=lambda message: message.text.lower() == "привет")
def send_greeting(message):
    bot.reply_to(message, "Привет! Рад тебя видеть!")
    

@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo = open('YOURPHOTO.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    
@bot.message_handler(commands=['keyboard'])
def send_keyboard(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Привет')
    itembtn2 = types.KeyboardButton('Пока')
    itembtn3 = types.KeyboardButton('Как дела?')
    itembtn4 = types.KeyboardButton('Помощь')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)

@bot.message_handler(commands=['stars'])
def send_stars(message):
    stars = "⭐️" * 5
    bot.reply_to(message, stars)

@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, "Почему программисты любят темную тему? Потому что светлое место не видно!")

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    sticker_id = 'CAACAgIAAxkBAAERKCNp9vvIf_Ukytxiiyy8FE-C5VUpewACDHMAAoJeKUmf_ZuXfNoHIjsE'
    bot.send_sticker(message.chat.id, sticker_id)


    
@bot.message_handler(func=lambda photo: True, content_types=['photo'])
def handle_photo(message):
    sticker_id = 'CAACAgIAAxkBAAERKCVp9wGYu6Wtmtj2-yKQgdKJVuqKIgACfJ8AAnH7MUscSgaI51nvqDsE'
    bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(commands=['links'])
def send_links(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Google", url="https://www.google.com"))
    markup.add(types.InlineKeyboardButton("YouTube", url="https://www.youtube.com"))
    bot.send_message(message.chat.id, "Полезные ссылки:", reply_markup=markup)
bot.polling()
