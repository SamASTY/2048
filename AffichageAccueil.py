import pygame
import sys

import Responsive as R
import Couleurs as C
import Param
import AffichageJeu
import SauvegardeScore as S
import AffichageScore

def PageAccueil():

    pygame.init()

    titre = Param.titre * 2
    taille_case = Param.taille_case

    largeur = Param.largeur *2
    hauteur = titre

    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("2048")

    # On utilise un index pour la sélection : 0=Jouer, 1=Score, 2=Quitter
    selection = 0

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selection = (selection + 1) % 3  # passe au bouton suivant
                elif event.key == pygame.K_LEFT:
                    selection = (selection - 1) % 3  # bouton précédent
                elif event.key == pygame.K_RETURN:
                    if selection == 0:  # Jouer
                        S.pseudoTmp = S.saisir_pseudo(fenetre)
                        AffichageJeu.jouer()
                    elif selection == 1:  # Score
                        AffichageScore.Score()
                    elif selection == 2:  # Quitter
                        running = False

        fenetre.fill((0, 0, 0))
        pygame.draw.rect(fenetre, C.GRIS_CLAIR, (0, 0, largeur, hauteur))

        texte = "2048"
        R.afficher_texte_multiligne(fenetre, texte, (largeur / 2.5, 5), Param.fontTitre, C.NOIR)

        espace = 20
        largeur_bouton = taille_case
        hauteur_bouton = taille_case
        total_width = 3 * largeur_bouton + 2 * espace
        start_x = (largeur - total_width) // 2
        y_pos = hauteur / 4

        bouton_jouer = pygame.Rect(start_x, y_pos, largeur_bouton, hauteur_bouton)
        bouton_score = pygame.Rect(start_x + largeur_bouton + espace, y_pos, largeur_bouton, hauteur_bouton)
        bouton_quitter = pygame.Rect(start_x + 2 * (largeur_bouton + espace), y_pos, largeur_bouton, hauteur_bouton)

        couleurs = [C.VERT_CLAIR, C.VERT_CLAIR, C.VERT_CLAIR]
        couleurs[selection] = C.VERT

        pygame.draw.rect(fenetre, couleurs[0], bouton_jouer)
        pygame.draw.rect(fenetre, couleurs[1], bouton_score)
        pygame.draw.rect(fenetre, couleurs[2], bouton_quitter)

        # Texte sur les boutons
        texte_jouer = Param.fontBouton.render("Jouer", True, C.NOIR)
        rect_jouer = texte_jouer.get_rect(center=bouton_jouer.center)
        fenetre.blit(texte_jouer, rect_jouer)

        texte_score = Param.fontBouton.render("Score", True, C.NOIR)
        rect_score = texte_score.get_rect(center=bouton_score.center)
        fenetre.blit(texte_score, rect_score)

        texte_quitter = Param.fontBouton.render("Quitter", True, C.NOIR)
        rect_quitter = texte_quitter.get_rect(center=bouton_quitter.center)
        fenetre.blit(texte_quitter, rect_quitter)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()