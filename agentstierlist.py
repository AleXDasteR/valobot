from bs4 import BeautifulSoup as bs
import requests


def trackerparse():
    url = 'https://tracker.gg/valorant/insights/agents'
    request = requests.get(url)
    soup = bs(request.text, 'html.parser')
    agents = soup.find_all('div', class_='value')
    print('Agent     PickRate Win%   Kills  KDR')
    for i in range(0, 105, 5):
        print(agents[i].text.ljust(9), agents[i + 1].text.ljust(8), agents[i + 2].text.ljust(6),
              agents[i + 3].text.ljust(6), agents[i + 4].text)


trackerparse()
