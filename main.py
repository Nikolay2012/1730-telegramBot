import telebot 
# подключаемся к боту (добовляем токен)
bot = telebot.TeleBot("5820978126:AAHL9UKbPXOMVdnB9PJTECN3YiYyIc_OlgQ")
# декоратор который выполняет сравнение команды старт с явно задоной в аргументе commands
@bot.message_handler(commands=["start"])
# функция обработчик сообщения 
def bot_start(message):
    # сообщение которое отправляет программа нашемо боту по id
    bot.send_message(message.chat.id, "Hello User!")

# команда которая ждет команды
bot.polling()
