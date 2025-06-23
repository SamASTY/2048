import Param
import pygame
import Couleurs as C

fichier = "score.txt"

pseudoTmp = " "

def save_score(pseudo, score, temps):
    scores = {}

    try:
        with open(fichier, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    old_pseudo, old_score, old_temps = parts
                    scores[old_pseudo] = (int(old_score), float(old_temps))
    except FileNotFoundError:
        pass

    if (pseudo not in scores) or (score > scores[pseudo][0]):
        scores[pseudo] = (score, temps)

    with open(fichier, "w") as file:
        for p, (s, t) in scores.items():
            file.write(f"{p},{s},{t}\n")

def charger_scores():
    scores = []
    try:
        with open("score.txt", "r") as file:
            for line in file:
                scores.append(line.strip())
    except FileNotFoundError:
        pass
    return scores


def draw_scores_list(surface, scores, offset):
    font = Param.fontCase
    ligne_height = font.get_height() + 10
    start_y = 100
    padding = 20

    zone_x = 10
    zone_y = start_y - 10
    zone_width = surface.get_width() - 2 * zone_x
    zone_height = surface.get_height() - start_y - 20

    pygame.draw.rect(surface, C.GRIS_CLAIR, (zone_x, zone_y, zone_width, zone_height), border_radius=10)

    for i, ligne in enumerate(scores):
        y = start_y + i * ligne_height + offset
        if zone_y <= y <= zone_y + zone_height - ligne_height:
            parts = ligne.split(",")
            if len(parts) == 3:
                pseudo, deplacements, temps = parts
                texte_a_afficher = f"{pseudo}, avec {deplacements} déplacement(s) en {temps} seconde(s)"
            else:
                texte_a_afficher = ligne

            text = Param.fontBouton.render(texte_a_afficher, True, C.NOIR)
            surface.blit(text, (zone_x + padding, y))



def draw_score(surface):
    text = Param.fontTitre.render(f"Score :", True, C.NOIR)
    text_rect = text.get_rect(center=(surface.get_width() // 2, 50))
    surface.blit(text, text_rect)


def draw_scrollbar(surface, offset, total_height, visible_height):
    if total_height <= visible_height:
        return

    bar_width = 10
    bar_x = surface.get_width() - bar_width - 5
    bar_height = max(30, visible_height * visible_height // total_height)
    scroll_pos = -offset * visible_height // total_height

    pygame.draw.rect(surface, C.VERT, (bar_x, 100, bar_width, visible_height), border_radius=5)
    pygame.draw.rect(surface, C.VERT_CLAIR, (bar_x, 100 + scroll_pos, bar_width, bar_height), border_radius=5)

def saisir_pseudo(fenetre):
    pygame.font.init()
    pseudo = ""
    actif = True
    clock = pygame.time.Clock()

    while actif:
        fenetre.fill((255, 255, 255))
        message = Param.fontBouton.render("Entrez votre pseudo : " + pseudo, True, (0, 0, 0))
        fenetre.blit(message, (20, 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                actif = False
                return None  # Abandon
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if pseudo.strip() != "":
                        actif = False
                elif event.key == pygame.K_BACKSPACE:
                    pseudo = pseudo[:-1]
                else:
                    pseudo += event.unicode

        clock.tick(30)
    return pseudo