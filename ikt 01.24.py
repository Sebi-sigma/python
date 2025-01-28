import random

def figurak(ertek,lista):
    db = 0
    for ertek in lista:
        db = db + 1
    return db


def fdb(mennyiseg):
    return len(mennyiseg)

def nyer(nyero,szin):
    if len(nyero)> len(fekete):
        szin = nyero
    return nyero







vel1 = random.randint(1,16)
vel2 = random.randint(1,16)
feher = []
fekete = []







for i in range(vel1):
    vel = random.randint(1,16)
    fekete.append(vel)


for i in range(vel2):
    vel = random.randint(1,16)
    feher.append(vel)



babuk = ['vezér, király, gyalog, futó,bástya,huszár']

print(f'A bábuk száma {figurak(1,babuk)}')
print(f'feketek száma 1 o utan: {fdb(feher)}')
print(f'feketek száma 1 o utan: {fdb(fekete)}')

print((f'nyert{nyer(szin)}'))








