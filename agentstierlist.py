from bs4 import BeautifulSoup as bs
import requests
import telebot

# region
token = '5611338157:AAFAZ0Jh7F-70b5RRJ_-3_pr3Y-X-zjxnJM'
bot = telebot.TeleBot(token)


# endregion

@bot.message_handler(commands=['tracker'])
def trackerparse(message):
    url = 'https://tracker.gg/valorant/insights/agents'
    request = requests.get(url)
    soup = bs(request.text, 'html.parser')
    agents = soup.find_all('div', class_='value')
    bot.send_message(message.chat.id, 'Agent     PickRate Win%   Kills  KDR')
    for i in range(0, 105, 5):
        bot.send_message(message.chat.id,
                         agents[i].text.ljust(9) + agents[i + 1].text.ljust(8) + agents[i + 2].text.ljust(6) +
                         agents[i + 3].text.ljust(6) + agents[i + 4].text)


trackerparse()
