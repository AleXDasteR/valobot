import telebot
from telebot import types
from perfectpickchoice import mappick as pick
from solopickbyclass import solopick as solo
from solopickbyclass import klassi as k
from solopickbyclass import maps as m
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


@bot.message_handler(commands=['tracker'])
def trackerparse(message):
    url = 'https://tracker.gg/valorant/insights/agents'
    request = requests.get(url)
    soup = Bs(request.text, 'html.parser')
    agents = soup.find_all('div', class_='value')
    bot.send_message(message.chat.id, 'Agent     PickRate Win%   Kills  KDR')
    for i in range(0, 105, 5):
        bot.send_message(message.chat.id,
                         agents[i].text.ljust(9) + agents[i + 1].text.center(8) + agents[i + 2].text.ljust(6) +
                         agents[i + 3].text.ljust(6) + agents[i + 4].text)


@bot.message_handler(content_types=['text'])
def perfmap(message):
    if message.text.split('+')[0].lower() in k and message.text.split('+')[1].lower() in m:
        bot.send_message(message.chat.id, solo(message.text))
    elif message.text.lower() in ['pearl', 'split', 'haven', 'lotus', 'fracture', 'ascent', 'icebox']:
        bot.send_message(message.chat.id, pick(message.text))


bot.infinity_polling()
