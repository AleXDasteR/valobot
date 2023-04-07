import os
import time

import telebot
from telebot import types
from perfectpickchoice import mappick as pick
from solopickbyclass import solopick as solo
from solopickbyclass import klassi as k
from solopickbyclass import maps as m
from trackerpic import trackerparse as t
import requests
from bs4 import BeautifulSoup as Bs

# region
token = '5611338157:AAFAZ0Jh7F-70b5RRJ_-3_pr3Y-X-zjxnJM'
bot = telebot.TeleBot(token)


# endregion


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Привет, я бот, дающий идеальные пики на карты, введи название карты на "
                     "английском и я дам тебе идеальный пик на карту или введи запрос в виде роль+map")


@bot.message_handler(commands=['help'])
def helper_command(message):
    bot.send_message(message.chat.id,
                     'Напиши эти сочетания чтобы получить полезные пики или информацию из трекера в онлайне!\n'
                     '1. /tracker - текущий тирлист агентов в валорант по винрейту со средними статами\n'
                     '2. "Haven" или любое другое название карты на английском - для получения идеального пика на данную карту\n'
                     '3. "защитник+Pearl", либо "защитник на Pearl", либо "защитник Pearl" - использовать можно любые сочетания роли и карты, пока что карта только на английском,а роль только на русском,но мы это доработаем)')


@bot.message_handler(commands=['tracker'])
def trackerparse(message):
    t()
    tracker_photo = open('C:/Users/Alexey/PycharmProjects/valobottelega/image.png', 'rb')
    bot.send_photo(message.chat.id, tracker_photo)


@bot.message_handler(content_types=['text'])
def perfmap(message):
    if (message.text.split('+')[0].lower() in k and message.text.split('+')[1].lower() in m) or \
            (message.text.split(' ')[0].lower() in k and message.text.split(' ')[1].lower() in m) or\
            (message.text.split(' на ')[0].lower() in k and message.text.split(' на ')[1].lower() in m):
        bot.send_message(message.chat.id, solo(message.text))
    elif message.text.lower() in ['pearl', 'split', 'haven', 'lotus', 'fracture', 'ascent', 'icebox']:
        bot.send_message(message.chat.id, pick(message.text))


bot.infinity_polling()
