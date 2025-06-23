import AffichageAccueil
import Param
import pygame
import Responsive as R

pygame.init()

info = pygame.display.Info()
Param.taille_max_fenetre = int(info.current_h * 0.5)
Param.taille_jeu = R.TailleJeu(Param.taille_max_fenetre)
Param.titre = R.TailleTitre(Param.taille_max_fenetre)
Param.taille_case = R.TailleCase(Param.taille_jeu)

Param.init_fonts()

largeur = Param.taille_jeu

AffichageAccueil.PageAccueil()
