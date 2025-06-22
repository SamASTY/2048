import random as rand
from traceback import extract_stack

HAUT = (-1, 0)
BAS = (1, 0)
GAUCHE = (0, -1)
DROITE = (0, 1)


def initTableau():
    tab = []
    for i in range(4):
        ligne = [0] * 4
        tab.append(ligne)
    ajouter_nouvelle_tuile(tab)
    ajouter_nouvelle_tuile(tab)
    return tab

def peut_jouer(tab, direction):
    delta_ligne, delta_col = direction
    n, m = 4, 4

    for i in range(n):
        for j in range(m):
            if tab[i][j] == 0:
                continue
            ni = i + delta_ligne
            nj = j + delta_col
            if 0 <= ni < n and 0 <= nj < m:
                if tab[ni][nj] == 0 or tab[ni][nj] == tab[i][j]:
                    return True
    return False

def Deplacer(tab, direction):
    delta_ligne, delta_col = direction
    n, m = 4, 4
    fusion = [[False]*m for _ in range(n)]
    moved = False
    lignes = range(n)
    colonnes = range(m)
    if direction == DROITE:
        colonnes = list(reversed(colonnes))
    elif direction == BAS:
        lignes = list(reversed(lignes))
    for i in lignes:
        for j in colonnes:
            if tab[i][j] == 0:
                continue
            x, y = i, j
            while True:
                ni = x + delta_ligne
                nj = y + delta_col
                if not (0 <= ni < n and 0 <= nj < m):
                    break
                if tab[ni][nj] == 0:
                    tab[ni][nj] = tab[x][y]
                    tab[x][y] = 0
                    x, y = ni, nj
                    moved = True
                elif tab[ni][nj] == tab[x][y] and not fusion[ni][nj]:
                    tab[ni][nj] *= 2
                    tab[x][y] = 0
                    fusion[ni][nj] = True
                    moved = True
                    break
                else:
                    break
    return moved

def EstJouable(tab, direction):
    delta_ligne, delta_col = direction
    n, m = 4, 4
    fusion = [[False]*m for _ in range(n)]
    moved = False
    lignes = range(n)
    colonnes = range(m)
    if direction == DROITE:
        colonnes = list(reversed(colonnes))
    elif direction == BAS:
        lignes = list(reversed(lignes))
    for i in lignes:
        for j in colonnes:
            if tab[i][j] == 0:
                continue
            x, y = i, j
            while True:
                ni = x + delta_ligne
                nj = y + delta_col
                if not (0 <= ni < n and 0 <= nj < m):
                    break
                if tab[ni][nj] == 0:
                    tab[ni][nj] = tab[x][y]
                    tab[x][y] = 0
                    x, y = ni, nj
                    moved = True
                elif tab[ni][nj] == tab[x][y] and not fusion[ni][nj]:
                    tab[ni][nj] *= 2
                    tab[x][y] = 0
                    fusion[ni][nj] = True
                    moved = True
                    break
                else:
                    break
    return moved


def ajouter_nouvelle_tuile(tab):
    cases_vides = [(i, j) for i in range(4) for j in range(4) if tab[i][j] == 0]
    if cases_vides:
        i, j = rand.choice(cases_vides)
        tab[i][j] = 2 if rand.random() < 0.9 else 4

def EnJeu(tab):
    return (peut_jouer(tab, HAUT) or
            peut_jouer(tab, BAS) or
            peut_jouer(tab, GAUCHE) or
            peut_jouer(tab, DROITE))