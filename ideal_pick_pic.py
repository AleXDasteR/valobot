from PIL import Image
import requests
from io import BytesIO
from perfectpickchoice import mappick as pick


def pick_pic(map_name):
    smokers = ['astra', 'brimstone', 'harbor', 'omen', 'viper']
    flashes = ['breach', 'fade', 'gekko', 'kayo', 'skye', 'sova']
    defenders = ['chamber', 'cypher', 'killjoy', 'sage']
    duelists = ['jett', 'neon', 'phoenix', 'raze', 'reyna', 'yoru']
    pick_dict = {smokers[
                     0]: 'https://static.wikia.nocookie.net/valorant/images/0/08/Astra_icon.png/revision/latest?cb=20210302164234',
                 smokers[
                     1]: 'https://static.wikia.nocookie.net/valorant/images/4/4d/Brimstone_icon.png/revision/latest?cb=20201128234311',
                 smokers[
                     2]: 'https://static.wikia.nocookie.net/valorant/images/f/f3/Harbor_icon.png/revision/latest?cb=20221018133629',
                 smokers[
                     3]: 'https://static.wikia.nocookie.net/valorant/images/b/b0/Omen_icon.png/revision/latest?cb=20201128234318',
                 smokers[
                     4]: 'https://static.wikia.nocookie.net/valorant/images/5/5f/Viper_icon.png/revision/latest?cb=20201128234408',
                 flashes[
                     0]: 'https://static.wikia.nocookie.net/valorant/images/5/53/Breach_icon.png/revision/latest?cb=20201128234328',
                 flashes[
                     1]: 'https://static.wikia.nocookie.net/valorant/images/a/a6/Fade_icon.png/revision/latest?cb=20220525095157',
                 flashes[
                     2]: 'https://static.wikia.nocookie.net/valorant/images/6/66/Gekko_icon.png/revision/latest?cb=20230307165000',
                 flashes[
                     3]: 'https://static.wikia.nocookie.net/valorant/images/f/f0/KAYO_icon.png/revision/latest?cb=20210622225019',
                 flashes[
                     4]: 'https://static.wikia.nocookie.net/valorant/images/3/33/Skye_icon.png/revision/latest?cb=20201128234628',
                 flashes[
                     5]: 'https://static.wikia.nocookie.net/valorant/images/4/49/Sova_icon.png/revision/latest?cb=20201128234221',
                 defenders[
                     0]: 'https://static.wikia.nocookie.net/valorant/images/0/09/Chamber_icon.png/revision/latest?cb=20211113013323',
                 defenders[
                     1]: 'https://static.wikia.nocookie.net/valorant/images/8/88/Cypher_icon.png/revision/latest?cb=20201128234211',
                 defenders[
                     2]: 'https://static.wikia.nocookie.net/valorant/images/1/15/Killjoy_icon.png/revision/latest?cb=20200805002141',
                 defenders[
                     3]: 'https://static.wikia.nocookie.net/valorant/images/7/74/Sage_icon.png/revision/latest?cb=20201128234057',
                 duelists[
                     0]: 'https://static.wikia.nocookie.net/valorant/images/3/35/Jett_icon.png/revision/latest?cb=20201128234156',
                 duelists[
                     1]: 'https://static.wikia.nocookie.net/valorant/images/d/d0/Neon_icon.png/revision/latest?cb=20220111220652',
                 duelists[
                     2]: 'https://static.wikia.nocookie.net/valorant/images/1/14/Phoenix_icon.png/revision/latest?cb=20201128234131',
                 duelists[
                     3]: 'https://static.wikia.nocookie.net/valorant/images/9/9c/Raze_icon.png/revision/latest?cb=20201128234400',
                 duelists[
                     4]: 'https://static.wikia.nocookie.net/valorant/images/b/b0/Reyna_icon.png/revision/latest?cb=20200607180311',
                 duelists[
                     5]: 'https://static.wikia.nocookie.net/valorant/images/d/d4/Yoru_icon.png/revision/latest?cb=20210112211830'}
    holst = Image.new('RGB', (1270, 256), color='#ffffff')
    karta = pick(map_name)
    x = 0
    for agent in karta:
        if agent not in ['chamber', 'gekko', 'harbor', 'sage', 'jett']:
            holst.paste(Image.open(BytesIO(requests.get(pick_dict[agent]).content)), (x, 0))
        elif agent in ['chamber', 'gekko', 'harbor']:
            holst.paste(Image.open(BytesIO(requests.get(pick_dict[agent]).content)).resize((256, 256)), (x, 0))
        elif agent == 'sage':
            holst.paste(Image.open(BytesIO(requests.get(pick_dict[agent]).content)).resize((264, 256)), (x, 0))
        elif agent == 'jett':
            holst.paste(Image.open(BytesIO(requests.get(pick_dict[agent]).content)).resize((264, 260)), (x, 0))
        x += 255
    holst.save('C:/Users/Alexey/PycharmProjects/valobottelega/perfectpick.png')
