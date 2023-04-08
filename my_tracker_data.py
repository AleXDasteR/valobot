from bs4 import BeautifulSoup as bs
import requests
import itertools
from PIL import Image, ImageDraw, ImageFont


def personal_profile(text):
    im = Image.new('RGB', (300, 415), color=('#FFDAB9'))
    text = text.split('#')
    name = text[0]
    tag = text[1]
    font = ImageFont.truetype('C:/Users/Alexey/Desktop/Aboreto-Regular.ttf', size=22, encoding='UTF-8')
    url = f'https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview'
    request = requests.get(url)
    soup = bs(request.text, 'html.parser')
    agents = soup.find_all('span', class_='value')
    stats = []
    for stat in agents:
        stats.append(stat.text)
    names = soup.find_all('span', class_='name')
    orig_names = []
    for name in names:
        orig_names.append(name.text)
    weapons = soup.find_all('div', class_='weapon__name')
    orig_weapons = []
    for weapon in weapons:
        orig_weapons.append(str(weapon.text) + ' kills')
    ans = list(itertools.chain(orig_weapons, orig_names[13:]))
    ans[9] = 'Ddelta/round'
    draw_text = ImageDraw.Draw(im)
    draw_text.text((65, -3), text='Overall stats', font=font, fill='#4B0082')
    for i in range(0, 380, 20):
        draw_text.text((5, i + 21), text=ans[i//20], font=font, fill='#4B0082')
    for i in range(0, 380, 20):
        draw_text.text((230, i + 21), text=stats[i // 20], font=font, fill='#4B0082')
    im.save('C:/Users/Alexey/PycharmProjects/valobottelega/personal_tracker.jpg')
