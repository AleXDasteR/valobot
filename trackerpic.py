from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup as bs
import requests


def trackerparse():
    url = 'https://tracker.gg/valorant/insights/agents'
    request = requests.get(url)
    soup = bs(request.text, 'html.parser')
    agents = soup.find_all('div', class_='value')
    im = Image.new('RGB', (640, 560), color=('#FFDAB9'))
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype('C:/Users/Alexey/Desktop/Aboreto-Regular.ttf', size=22)
    draw_text.text(
        (0, 0),
        'Agent      PickRate           Win%            Kills              KDR',
        font=font,
        fill=('#7B68EE')
    )
    for i in range(0, 525, 25):
        formatted = [agents[i // 5].text.ljust(9), agents[i // 5 + 1].text.ljust(8), agents[i // 5 + 2].text.ljust(6),
                     agents[i // 5 + 3].text.ljust(6), agents[i // 5 + 4].text]
        for j in range(0, 5):
            draw_text.text(
                (j * 140, i + 50),
                font=font,
                text=formatted[j],
                anchor='ls',
                fill=('#7B68EE')
            )
    im.save('C:/Users/Alexey/PycharmProjects/valobottelega/image.png')
