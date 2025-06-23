import pygame

taille_max_fenetre = None
taille_jeu = None
titre = 200
taille_case = None
largeur = 200


def init_fonts():
    global fontTitre, fontBouton, fontCase
    if titre is None:
        raise ValueError("La variable 'titre' doit être initialisée avant d'appeler init_fonts()")
    fontTitre = pygame.font.SysFont(None, int(titre * 0.4))
    fontBouton = pygame.font.SysFont(None, int(titre * 0.3))
    fontCase = pygame.font.SysFont(None, int(titre * 0.2))