from PIL import Image, ImageDraw, ImageFont
from perfectpickchoice import mappick as pick


def pick_pic(map_name):
    smokers = ['astra', 'brimstone', 'harbor', 'omen', 'viper']
    flashes = ['breach', 'fade', 'gekko', 'kayo', 'skye', 'sova']
    defenders = ['chamber', 'cypher', 'killjoy', 'sage']
    duelists = ['jett', 'neon', 'phoenix', 'raze', 'reyna', 'yoru']
    pick_dict = {smokers[
                     0]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Astra_icon.png',
                 smokers[
                     1]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Brimstone_icon.png',
                 smokers[
                     2]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Harbor_icon.png',
                 smokers[
                     3]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Omen_icon.png',
                 smokers[
                     4]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Viper_icon.png',
                 flashes[
                     0]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Breach_icon.png',
                 flashes[
                     1]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Fade_icon.png',
                 flashes[
                     2]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Gekko_icon.png',
                 flashes[
                     3]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/KAYO_icon.png',
                 flashes[
                     4]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Skye_icon.png',
                 flashes[
                     5]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Sova_icon.png',
                 defenders[
                     0]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Chamber_icon.png',
                 defenders[
                     1]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Cypher_icon.png',
                 defenders[
                     2]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Killjoy_icon.png',
                 defenders[
                     3]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Sage_icon.png',
                 duelists[
                     0]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Jett_icon.png',
                 duelists[
                     1]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Neon_icon.png',
                 duelists[
                     2]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Phoenix_icon.png',
                 duelists[
                     3]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Raze_icon.png',
                 duelists[
                     4]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Reyna_icon.png',
                 duelists[
                     5]: 'C:/Users/Alexey/PycharmProjects/valobottelega/icons/Yoru_icon.png'}
    holst = Image.new('RGB', (620, 1400), color='#FFDAB9')
    karta = pick(map_name)
    font = ImageFont.truetype('C:/Users/Alexey/Desktop/Aboreto-Regular.ttf', size=60)
    draw_text = ImageDraw.Draw(holst)
    x = 70
    for agent in karta:
        draw_text.text((300, 60), text=map_name, font=font, fill=('#4B0082'), anchor='ms')
        tracker_photo = Image.open(pick_dict[agent]).resize((256, 256))
        holst.paste(tracker_photo, (0, x), mask=tracker_photo.convert('RGBA'))
        draw_text.text((260, x + 100), agent.title(), font=font, fill=('#4B0082'))
        x += 270
    holst.save('C:/Users/Alexey/PycharmProjects/valobottelega/perfectpick.png')
