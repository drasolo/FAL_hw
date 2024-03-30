# citire
import copy
f = open("input.in", 'r')
date_intrare = f.read().split('\n')
f.close()

# construire dict automat ?? yey

automat = {}
starifinale = []
cuvinte = []
cititstare = False

for linie in date_intrare:
    print(automat)
    linie = linie.split()
    if len(linie) > 2:
        if linie[1][0] != 'q':
            if linie[2] not in automat:
                automat[linie[2]] = [tuple([linie[0], linie[1]])]
            else:
                automat[linie[2]].append(tuple([linie[0], linie[1]]))
    try:
        if linie[1][0] == 'q' or (len(linie) == 1):
            for stare_finala in linie:
                starifinale.append(stare_finala)
                cititstare = True
    except:
        if len(linie) == 1:
            if cititstare == False:
                starifinale.append(linie[0])
                cititstare = True
            else:
                cuvinte.append(linie[0])

# prima iteratie

Q = []

for stare in starifinale:
    Q.append([stare, ""])

cuvintebunepoate = []

for lungime in range(int(cuvinte[0])+2):
    print(Q)
    for el in copy.deepcopy(Q):
        Q.pop(0)
        if len(Q) > 20:
            break
        if el[0] != 'q0':
            for previous in automat[el[0]]:
                new_element = [previous[0], previous[1] + el[1]]
                Q.append(new_element)
        else:
            if lungime == int(cuvinte[0]):
                cuvintebunepoate.append(el[1])


print(*cuvintebunepoate)




