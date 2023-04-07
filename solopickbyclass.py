import random

maps = ['pearl', 'split', 'haven', 'lotus', 'fracture', 'ascent', 'icebox']
klassi = ['смоки', 'флешки', 'защитник', 'дуэлянт']


def solopick(klass):
    if klass.count('+') == 1:
        agents = klass.lower().split('+')
    elif klass.count('на') == 1:
        agents = klass.lower().split(' на ')
    else:
        agents = klass.lower().split(' ')
    smokers = ['Astra', 'Brimstone', 'Harbor', 'Omen', 'Viper']  # список всех агентов по классам
    flashes = ['Breach', 'Fade', 'Gekko', 'KAY/O', 'Skye', 'Sova']
    defenders = ['Chamber', 'Cypher', 'Killjoy', 'Sage']
    duelists = ['Jett', 'Neon', 'Phoenix', 'Raze', 'Reyna', 'Yoru']
    perfectpick = {maps[0]: [smokers[0], flashes[3], defenders[3], duelists[1], duelists[2]],
                   maps[1]: [smokers[1], flashes[0], defenders[3], duelists[3], duelists[2]],
                   maps[2]: [smokers[0], random.choice(flashes), defenders[3], duelists[0], duelists[4]],
                   maps[3]: [smokers[0], flashes[2], defenders[2], duelists[5], duelists[random.randint(0, 2)]],
                   maps[4]: [smokers[1], 'KAY/O or Breach', defenders[random.randint(1, 2)], duelists[1], duelists[
                       2]],
                   maps[5]: ['Brimstone or Omen', flashes[random.randint(4, 5)], defenders[2], duelists[0], duelists[
                       2]],
                   maps[6]: [smokers[4], 'KAY/O or Sova', defenders[3], duelists[0], duelists[1]]}
    if agents[0] == 'смоки':
        return perfectpick[agents[1]][0]
    elif agents[0] == 'флешки':
        return perfectpick[agents[1]][1]
    elif agents[0] == 'защитник':
        return perfectpick[agents[1]][2]
    elif agents[0] == 'дуэлянт':
        return perfectpick[agents[1]][3] + ' или ' + perfectpick[agents[1]][4]
