import random



def fdb(mennyiseg):
    return len(mennyiseg)

def nyer(feher,fekete):
    if len(feher)> len(fekete):
        return ' nyert a feher '
    elif len(feher) == len(fekete):
        return 'döntetlen'
    else:
        return 'nyert a fekete '





ujra = "igen"
while ujra == "igen":
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



    babuk = ['vezér, király, gyalog, futó, bástya, huszár']

    print(f' a bábuk száma: ',len(fekete) + len(feher))
    print(f'fehérek száma 1 o utan: {fdb(feher)}')
    print(f'feketek száma 1 o utan: {fdb(fekete)}')

    print(f'{nyer(feher,fekete)}')

#próba
#sor = 1
#while sor <= 8:
#     oszlop = 1
#     while oszlop <= 8:
#     # print('')
#         if oszlop == 4 and sor == 1:
 #            print("X",end=' ')
#         elif oszlop == 7 and sor == 2:
#             print("X")
#         elif oszlop == 3 and sor == 3:
#             print("X")
#         elif oszlop == 8 and sor == 4:
#             print("X",end=' ')
#         elif oszlop == 2 and sor == 5:
#             print("X")
#         elif oszlop == 5 and sor == 6:
#             print("X")
#         elif oszlop == 1 and sor == 7:
#             print("X")
#         elif oszlop == 6 and sor == 8:
#             print("X")
#sor = sor + 1
#oszlop = oszlop + 1


    ujra = input("Szeretnél újra játszani? (igen/nem): ").strip().lower()


osszefuz=''
for i in range(8):
    osszefuz = ''
    for j in range(8):
        if i == 0 and j == 3:
            osszefuz += 'X '
        elif i == 1 and j == 6:
            osszefuz += 'X '
        elif i == 2 and j == 2:
            osszefuz += 'X '
        elif i == 3 and j == 7:
            osszefuz += 'X '
        elif i == 4 and j == 1:
            osszefuz += 'X '
        elif i == 5 and j == 4:
            osszefuz += 'X '
        elif i == 6 and j == 0:
            osszefuz += 'X '
        elif i == 7 and j == 5:
            osszefuz += 'X '
        else:
            osszefuz += 'O '
    print(osszefuz)












