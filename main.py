import telebot 
import random

# подключаемся к боту (добовляем токен)
bot = telebot.TeleBot("5452132659:AAGfkHs7Olu2Mn0I04cX5CT2vO_mkA3w2E4")
#
# отримати опис бота, його характеристики
user = bot.get_me()
# відправити посилання до чату бота
# bot.send_message(214356301, "Задай команду '/start', щоб почати роботу")
#
bt1 = telebot.types.KeyboardButton("Play")
#
menu_bar = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)
#
menu_bar.add(bt1)
# декоратор который выполняет сравнение команды старт с явно задоной в аргументе commands
@bot.message_handler(commands=["start"])
# функция обработчик сообщения 
def bot_start(message):
    # сообщение которое отправляет программа нашемо боту по id
    bot.send_message(message.chat.id, "Hello User", reply_markup= menu_bar)
    # print(message.chat.id)
    bot.register_next_step_handler(message, press_play)
# команда которая ждет команды 
def press_play(message):
    if message.text == "Play":
        menu_bar1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard= True)
        number = random.randint(1, 4)
        bt_num1 = telebot.types.KeyboardButton("1")
        bt_num2 = telebot.types.KeyboardButton("2")
        bt_num3 = telebot.types.KeyboardButton("3")
        # menu_bar1.add(bt_num1)
        menu_bar1.add(bt_num1, bt_num2, bt_num3)
        # menu_bar1.add(bt_num2)
        # menu_bar1.add(bt_num3)
        bot.send_message(message.chat.id, "Game started", reply_markup= menu_bar1)
        bot.register_next_step_handler(message, win_or_over, number)
    if "Пр" in message.text:
        bot.send_message(message.chat.id, "Здоровенькі були")
        bot.register_next_step_handler(message, press_play)

def win_or_over(message, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, "Відповідь зараховано!")
    else:
        bot.send_message(message.chat.id, "Ви не вгадали!", reply_markup= menu_bar)
        bot.register_next_step_handler(message, press_play)
      
bot.polling()

