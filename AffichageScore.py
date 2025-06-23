import pygame
import sys

import Param
import Couleurs as C
import SauvegardeScore as S
import AffichageAccueil

def Score():
    pygame.init()

    taille_jeu = Param.taille_jeu

    Param.init_fonts()
    largeur = taille_jeu*2
    hauteur = taille_jeu
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("2048")

    clock = pygame.time.Clock()

    scroll_offset = 0
    score_lines = S.charger_scores()
    running = True

    while running:
        fenetre.fill(C.BLANC)
        ligne_height = Param.fontCase.get_height() + 10
        total_height = len(score_lines) * ligne_height
        visible_height = hauteur - 100 - 30

        offset_max = max(0, total_height - visible_height)
        scroll_offset = max(-offset_max, min(0, scroll_offset))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                AffichageAccueil.PageAccueil()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    scroll_offset -= 20
                elif event.key == pygame.K_UP:
                    scroll_offset += 20

            if event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * 20
        S.draw_score(fenetre)
        S.draw_scores_list(fenetre, score_lines, scroll_offset)
        S.draw_scrollbar(fenetre, scroll_offset, total_height, visible_height)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
