import telebot
from main import get_link, parse, parse_data_music, clean

token = '1129978255:AAFDhGIvzn5s0YzBDGe214o8JsbnxYetb2w'
bot = telebot.TeleBot(token)


def get_track_name(message):
    return message.text


@bot.message_handler(commands=['start','help'])
def meet_user(message):
        bot.send_message(message.chat.id,
                     "Привет, я бот для закачки музыки на твое устройство, введи название песни, а я попытаюсь ее найти)")


# нужен обработчик
@bot.message_handler(content_types=['text'])
def send_track_url(message):
    clean()
    try:
        parse(get_link(message.text))
        bot.send_message(message.chat.id, parse_data_music())
    except:
        bot.send_message(message.chat.id,'Такой песни нет, введите корректное название')


bot.polling(none_stop=True, interval=0)
