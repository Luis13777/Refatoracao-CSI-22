import pygame
from scripts.data import *
from scripts.run import *
from scripts.init import *
from scripts.auxFuncs import *


def main_menu():

    window = DISPLAY["pygameDisplay"]

    click = False
    while True:

        window.fill((0, 255, 100))
        window.blit(IMAGENS["BACKGROUND"]["pygameImage"], (0,0))
        window.blit(IMAGENS["BONECO2"]["pygameImage"], (140,80))
        window.blit(IMAGENS["BONECO1"]["pygameImage"], (530,80))

        draw_text('Bomber Smash', FONTS["BIG"]["pygameFont"], (255, 255, 255), window, 155, 100)

        draw_text('CONTROLES P1', FONTS["NORMAL"]["pygameFont"], (255, 255, 255), window, 10, 175)
        draw_text('SETAS', FONTS["NORMAL"]["pygameFont"], (255, 255, 255), window, 10, 260)
        draw_text('BOMBA: SHIFT', FONTS["NORMAL"]["pygameFont"], (255, 255, 255), window, 10, 300)

        draw_text('CONTROLES P2', FONTS["NORMAL"]["pygameFont"], (255, 255, 255), window, 450, 175)
        draw_text('WASD', FONTS["NORMAL"]["pygameFont"], (255, 255, 255), window, 450, 260)
        draw_text('BOMBA: ESPAÇO', FONTS["NORMAL"]["pygameFont"], (255, 255, 255), window, 450, 300)

        # ----- Configura os botões clicáveis
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(275, 400, 200, 50)
        button_2 = pygame.Rect(275, 500, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
                
        pygame.draw.rect(window, (255, 0, 0), button_1)
        pygame.draw.rect(window, (255, 0, 0), button_2)
        draw_text('JOGAR', FONTS["NORMAL"]["pygameFont"], (0, 0, 0), window, 310, 410)
        draw_text('SAIR', FONTS["NORMAL"]["pygameFont"], (0, 0, 0), window, 330, 510)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()