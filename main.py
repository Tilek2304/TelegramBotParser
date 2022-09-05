import json
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

@bot.message_handler()
def get_news_num(message):
    for i in get_news_list():
        # print(i['id'])
        if message.text == i['id']:
            html = parse_news_page(i['link'])
            text = ''
            for i in html:
                string = i.find_all('p')
                for j in string:
                    text += j.text
                bot.send_message(message.chat.id, text, parse_mode='html')
                string = j.find_all('img', class_='Gallery--single-image-img ls-is-cached lazyloaded')
                for k in string:
                    bot.send_message(message.chat.id, k.get('src'), parse_mode='html')
    return None

bot.polling(non_stop=True)