
from socket import htonl
import telebot
from parseFile import get_news_list, parse_news_page

bot = telebot.TeleBot('5731607325:AAG2_l4SjLQYEHaFY-KGBScMR2eyeKiSSz0')

@bot.message_handler(commands=['start'])
def start(message):
    mess = get_news_list()
    temp = 0
    for i in mess:
        temp +=1
        id_ = i.get('id')
        title = i.get('title')
        bot.send_message(message.chat.id, f'{id_}: {title}', parse_mode='html')
        if temp >= 20:
            bot.send_message(message.chat.id,"some title news you can see Description of this news and Photo", parse_mode='html')
            return None

@bot.message_handler
def get_news_num(message):
    for i in get_news_list():
        if message.text == i.get('id'):
            html = parse_news_page(i.get('link'))
            bot.send_message(message.chat.id, html, parse_mode='html')
        else:
            bot.send_message(message.chat.id, 'нет такой новости', parse_mode='html')
            return None


bot.polling(non_stop=True)