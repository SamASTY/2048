def TailleJeu(taille_max_fenetre):
    taille = int(taille_max_fenetre * 0.6)
    return taille - (taille % 4)

def TailleCase(taille_jeu):
    return taille_jeu // 4

def TailleTitre(taille_max_fenetre):
    return int(taille_max_fenetre * 0.15)

def GenererTableau(taille_case, hauteur_titre):
    coordonnees_cases = []
    for i in range(4):
        ligne = []
        for j in range(4):
            x = j * taille_case
            y = hauteur_titre + i * taille_case
            ligne.append((x, y))
        coordonnees_cases.append(ligne)
    return coordonnees_cases

def afficher_texte_multiligne(surface, texte, position, font, couleur):
    lignes = texte.split('\n')
    x, y = position
    for i, ligne in enumerate(lignes):
        img_texte = font.render(ligne, True, couleur)
        surface.blit(img_texte, (x, y + i * (font.get_linesize())))
