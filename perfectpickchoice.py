import random


def mappick(name):
    map1 = str(name).lower()
    maps = ['pearl', 'split', 'haven', 'lotus', 'fracture', 'ascent', 'icebox']  # список карт в игре
    # agents = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 'Fade', 'Gekko', 'Harbor',
    #          'Jett', 'KAY/O', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage',
    #          'Skye', 'Sova', 'Viper', 'Yoru']
    smokers = ['astra', 'brimstone', 'harbor', 'omen', 'viper']  # список всех агентов по классам
    flashes = ['breach', 'fade', 'gekko', 'kayo', 'skye', 'sova']
    defenders = ['chamber', 'cypher', 'killjoy', 'sage']
    duelists = ['jett', 'neon', 'phoenix', 'raze', 'reyna', 'yoru']
    # составление идельных пиков для каждой из карт в игре
    perfectpick = {maps[0]: [smokers[0], flashes[3], defenders[3], duelists[1], duelists[2]],
                   maps[1]: [smokers[1], flashes[0], defenders[3], duelists[3], duelists[2]],
                   maps[2]: [smokers[0], random.choice(flashes), defenders[3], duelists[0], duelists[4]],
                   maps[3]: [smokers[0], flashes[2], defenders[2], duelists[5], duelists[random.randint(0, 3)]],
                   maps[4]: [smokers[1], flashes[0], defenders[random.randint(1, 2)], duelists[1], duelists[
                       2]],
                   maps[5]: [smokers[3], flashes[random.randint(4, 5)], defenders[2], duelists[0], duelists[
                       2]],
                   maps[6]: [smokers[4], flashes[3], defenders[3], duelists[0], duelists[1]]}
    if map1 in maps:
        return perfectpick[map1]
