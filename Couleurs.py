GRIS_CLAIR = (238, 228, 218)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
JAUNE_CLAIR = (249, 246, 242)
JAUNE = (255, 235, 156)
VERT_CLAIR = (180, 230, 180)
VERT_MOYEN = (120, 200, 120)
VERT = (60, 170, 60)
VERT_FONCE = (0, 128, 0)
VERT_TRES_FONCE = (0, 100, 0)
VERT_TRES_SOMBRE = (0, 70, 0)

def couleur_case(valeur):
    couleurs = {
        0: BLANC,
        2: JAUNE_CLAIR,
        4: JAUNE,
        8: VERT_CLAIR,
        16: VERT_MOYEN,
        32: VERT,
        64: VERT_FONCE,
        128: VERT_TRES_FONCE,
        256: VERT_TRES_SOMBRE,
        512: (0, 50, 0),
        1024: (0, 40, 0),
        2048: (0, 30, 0),
    }
    return couleurs.get(valeur, NOIR)
