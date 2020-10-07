import telebot

token = '1129978255:AAFDhGIvzn5s0YzBDGe214o8JsbnxYetb2w'
bot = telebot.TeleBot(token)


def get_track_name(message):
    return message.text


@bot.message_handler(commands=['start'])
def meet_user(message):
    bot.send_message(message.chat.id,
                     "Привет, я бот для закачки музыки на твое устройство, введи название песни, а я попытаюсь ее найти)")


@bot.message_handler(content_types=['text'])
def send_track_url(message):
    get_track_name(message)
    # присылать ссылку


bot.polling(timeout=600)
