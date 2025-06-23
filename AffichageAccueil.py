import Responsive as R
import Couleurs as C
import TableauJeu as T
import Param
import pygame
import sys
import AffichageJeu

def PageAccueil():

    pygame.init()

    titre = Param.titre * 2
    taille_case = Param.taille_case


    largeur = Param.largeur
    hauteur = titre

    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("2048")

    Jouer = True

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if Jouer:
                        AffichageJeu.jouer()
                    else:
                        running = False
                elif event.key == pygame.K_LEFT:
                    if not Jouer:
                        Jouer = True
                elif event.key == pygame.K_RIGHT:
                    if Jouer:
                        Jouer = False


        fenetre.fill((0, 0, 0))

        pygame.draw.rect(fenetre, C.GRIS_CLAIR, (0, 0, largeur, hauteur))

        texte = "2048"
        R.afficher_texte_multiligne(fenetre, texte, (largeur / 2.5, 5), Param.fontTitre, C.NOIR)

        bouton_jouer = pygame.Rect(5, hauteur / 4, taille_case, taille_case)
        bouton_quitter = pygame.Rect(largeur - taille_case - 5, hauteur / 4, taille_case, taille_case)

        if Jouer:
            pygame.draw.rect(fenetre, C.VERT, bouton_jouer)
            pygame.draw.rect(fenetre, C.VERT_CLAIR, bouton_quitter)
        else:
            pygame.draw.rect(fenetre, C.VERT_CLAIR, bouton_jouer)
            pygame.draw.rect(fenetre, C.VERT, bouton_quitter)

        texte_jouer = Param.fontBouton.render("Jouer", True, C.NOIR)
        rect_jouer = texte_jouer.get_rect(center=bouton_jouer.center)
        fenetre.blit(texte_jouer, rect_jouer)

        texte_quitter = Param.fontBouton.render("Quitter", True, C.NOIR)
        rect_quitter = texte_quitter.get_rect(center=bouton_quitter.center)
        fenetre.blit(texte_quitter, rect_quitter)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()