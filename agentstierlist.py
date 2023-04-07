from bs4 import BeautifulSoup as bs
import requests
import telebot

# region
token = '5611338157:AAFAZ0Jh7F-70b5RRJ_-3_pr3Y-X-zjxnJM'
bot = telebot.TeleBot(token)


# endregion
def trackerparse():
    url = 'https://tracker.gg/valorant/insights/agents'
    request = requests.get(url)
    soup = bs(request.text, 'html.parser')
    agents = soup.find_all('div', class_='value')
    print('Agent     PickRate Win%   Kills  KDR')
    for i in range(0, 105, 5):
        print(agents[i].text.ljust(9), agents[i + 1].text.ljust(8), agents[i + 2].text.ljust(6),
              agents[i + 3].text.ljust(6), agents[i + 4].text)


def most_popular(role):
    url = 'https://tracker.gg/valorant/insights/agents'
    request = requests.get(url)
    soup = bs(request.text, 'html.parser')
    agents = soup.find_all('div', class_='value')
    dict_person = {}
    for i in range(0, 105, 5):
        if agents[i].text in ['Astra', 'Brimstone', 'Harbor', 'Omen', 'Viper']:
            dict_person['smokers'] = dict_person.get('smokers', {}) | {agents[i].text:
                                                                           [float(agents[i + 1].text[:-1]),
                                                                            float(agents[i + 2].text[:-1]),
                                                                            float(agents[i + 3].text[:-1]),
                                                                            float(agents[i + 4].text)]}
        elif agents[i].text in ['Breach', 'Fade', 'Gekko', 'KAY/O', 'Skye', 'Sova']:
            dict_person['flashes'] = dict_person.get('flashes', {}) | {agents[i].text:
                                                                           [float(agents[i + 1].text[:-1]),
                                                                            float(agents[i + 2].text[:-1]),
                                                                            float(agents[i + 3].text[:-1]),
                                                                            float(agents[i + 4].text)]}
        elif agents[i].text in ['Chamber', 'Cypher', 'Killjoy', 'Sage']:
            dict_person['defenders'] = dict_person.get('defenders', {}) | {agents[i].text:
                                                                               [float(agents[i + 1].text[:-1]),
                                                                                float(agents[i + 2].text[:-1]),
                                                                                float(agents[i + 3].text[:-1]),
                                                                                float(agents[i + 4].text)]}
        else:
            dict_person['dualist'] = dict_person.get('dualist', {}) | {agents[i].text:
                                                                           [float(agents[i + 1].text[:-1]),
                                                                            float(agents[i + 2].text[:-1]),
                                                                            float(agents[i + 3].text[:-1]),
                                                                            float(agents[i + 4].text)]}

    return dict_person[role]


role = input()
print(most_popular(role))
