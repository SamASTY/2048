import pygame
import sys

import Responsive as R
import Couleurs as C
import TableauJeu as T
import Param
import AffichageAccueil
import SauvegardeScore as S


def jouer():
    pygame.init()

    taille_jeu = Param.taille_jeu
    taille_case = Param.taille_case
    titre = Param.titre

    Param.init_fonts()

    tableau = R.GenererTableau(taille_case, titre)

    largeur = taille_jeu
    hauteur = titre + taille_jeu

    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("2048")

    Deplacement = 0
    temps_debut = pygame.time.get_ticks()
    txt = "2048\n"

    valeurs = T.initTableau()

    clock = pygame.time.Clock()
    running = True
    while running:

        for event in pygame.event.get():
            if running == False:
                S.save_score(S.pseudoTmp, Deplacement,Temps)
                AffichageAccueil.PageAccueil()
            if event.type == pygame.QUIT:
                running = False
                AffichageAccueil.PageAccueil()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if T.peut_jouer(valeurs, T.HAUT):
                        T.Deplacer(valeurs, T.HAUT)
                        T.ajouter_nouvelle_tuile(valeurs)
                        Deplacement += 1
                elif event.key == pygame.K_DOWN:
                    if T.peut_jouer(valeurs, T.BAS):
                        T.Deplacer(valeurs, T.BAS)
                        T.ajouter_nouvelle_tuile(valeurs)
                        Deplacement += 1
                elif event.key == pygame.K_LEFT:
                    if T.peut_jouer(valeurs, T.GAUCHE):
                        T.Deplacer(valeurs, T.GAUCHE)
                        T.ajouter_nouvelle_tuile(valeurs)
                        Deplacement += 1
                elif event.key == pygame.K_RIGHT:
                    if T.peut_jouer(valeurs, T.DROITE):
                        T.Deplacer(valeurs, T.DROITE)
                        T.ajouter_nouvelle_tuile(valeurs)
                        Deplacement += 1
                running = T.EnJeu(valeurs)

        fenetre.fill((0, 0, 0))

        pygame.draw.rect(fenetre, C.GRIS_CLAIR, (0, 0, largeur, titre))

        temps_ecoule_ms = pygame.time.get_ticks() - temps_debut
        Temps = temps_ecoule_ms // 1000
        texte_change = f"Deplacement : {Deplacement}\nTemps : {Temps} seconde"

        R.afficher_texte_multiligne(fenetre, txt, (largeur / 3, 5), Param.fontTitre, C.NOIR)
        R.afficher_texte_multiligne(fenetre, texte_change, (0, titre / 3), Param.fontBouton, C.NOIR)

        for i, ligne in enumerate(tableau):
            for j, (x, y) in enumerate(ligne):
                valeur = valeurs[i][j]
                couleur = C.couleur_case(valeur)
                pygame.draw.rect(fenetre, couleur, (x, y, taille_case, taille_case))

                if valeur != 0:
                    texte_valeur = Param.fontBouton.render(str(valeur), True, C.NOIR)
                    rect_texte = texte_valeur.get_rect(center=(x + taille_case // 2, y + taille_case // 2))
                    fenetre.blit(texte_valeur, rect_texte)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
