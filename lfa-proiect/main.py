import copy

# Citire
f = open("input.in", 'r')
date_intrare = f.read().split('\n')
f.close()

# Inițializare automat și stări finale
automat = {}
stari_finale = []
cuvinte = []
citit_stare = False

# Construirea automatului
for linie in date_intrare:
    linie = linie.split()
    if len(linie) > 2:
        if tuple([linie[0], linie[1]]) not in automat:
            automat[tuple([linie[0], linie[1]])] = [linie[2]]
        else:
            automat[tuple([linie[0], linie[1]])].append(linie[2])
    try:
        if linie[1][0] == 'q' or (len(linie) == 1):
            for stare_finala in linie:
                stari_finale.append(stare_finala)
                citit_stare = True
    except:
        if len(linie) == 1:
            if citit_stare == False:
                stari_finale.append(linie[0])
                citit_stare = True
            else:
                cuvinte.append(linie[0])

# Funcție pentru căutarea cuvintelor în automat
def search_in_automaton(cuvant):
    Q = [['q0', cuvant, []]]
    while len(Q) > 0:
        current_state, remaining_word, path = Q.pop(0)
        if current_state in stari_finale:
            path.append(current_state)
            print("Accepted:", path)
            return True
        if len(remaining_word) > 0:
            if (current_state, remaining_word[0]) in automat:
                for next_state in automat[(current_state, remaining_word[0])]:
                    new_path = copy.deepcopy(path)
                    new_path.append(current_state)
                    Q.append([next_state, remaining_word[1:], new_path])
    print("Rejected")
    return False

# Căutarea cuvintelor în automat
for cuvant in cuvinte:
    if not search_in_automaton(cuvant):
        print("Word '{}' was not accepted.".format(cuvant))
