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
        draw_text.text((5, i + 21), text=ans[i // 20], font=font, fill='#4B0082')
    for i in range(0, 380, 20):
        draw_text.text((230, i + 21), text=stats[i // 20], font=font, fill='#4B0082')
    im.save('C:/Users/Alexey/PycharmProjects/valobottelega/personal_tracker.jpg')
    return stats


def statistic_personal(name):
    stata = personal_profile(name)
    stata_full = {'ADR': float(stata[3]) >= 140, 'KDR': float(stata[4]) >= 1.00, 'HSR': int(stata[5][:2]) >= 17,
                  'KAST': int(stata[8][:2]) >= 75, 'ACS': float(stata[13]) >= 200, 'KDA': float(stata[14]) >= 1.25}
    if stata_full['ADR'] and stata_full['KDR'] and stata_full['HSR'] and stata_full['KAST'] and stata_full['ACS'] and \
            stata_full['KDA']:
        return 'Ваши показатели статистики полностью соответсвуют или обгоняют средние статы, поэтому можно сказать,что вы отыгрываете прекрасно в этом акте!'
    elif stata_full['ADR'] and stata_full['KDR'] and stata_full['HSR'] and not stata_full['KAST'] and stata_full['ACS'] \
            and stata_full['KDA']:
        return 'Вы неплохо отыгрываете текущий акт, но не используете все необходимые способности для победы,старайтесь чаще нажимать ваши кнопки в раундах!'
    elif stata_full['ADR'] and stata_full['KDR'] and stata_full['HSR'] and stata_full['KAST'] and not stata_full['ACS'] \
            and stata_full['KDA']:
        return
    elif not stata_full['ADR'] and stata_full['KDR'] and stata_full['HSR'] and stata_full['KAST'] and stata_full['ACS'] \
            and stata_full['KDA']:
        return
    elif stata_full['ADR'] and not stata_full['KDR'] and stata_full['HSR'] and stata_full['KAST'] and stata_full['ACS'] \
            and stata_full['KDA']:
        return
    elif stata_full['ADR'] and stata_full['KDR'] and not stata_full['HSR'] and stata_full['KAST'] and stata_full['ACS'] \
            and stata_full['KDA']:
        return 'У вас неплохие действия по игре и вы играете довольно импактно для команды,но вам не хватает аима для быстрых убийств!'
    elif stata_full['ADR'] and stata_full['KDR'] and stata_full['HSR'] and stata_full['KAST'] and stata_full['ACS'] \
            and not stata_full['KDA']:
        return 'Вы либо соло игрок, либо очень мало помогаете по игре своим тиммейтам, так что вы знаете что делать)'
