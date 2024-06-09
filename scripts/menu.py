import pygame
from scripts.data import *
from scripts.run import *
from scripts.init import *


def main_menu():
    click = False
    while True:

        window.fill((0, 255, 100))
        window.blit(bg_img, (0,0))
        window.blit(boneco1_img, (140,80))
        window.blit(boneco_img, (530,80))
        draw_text('Bomber Smash', title, (255, 255, 255), window, 155, 100)

        draw_text('CONTROLES P1', font, (255, 255, 255), window, 10, 175)
        draw_text('SETAS', font, (255, 255, 255), window, 10, 260)
        draw_text('BOMBA: SHIFT', font, (255, 255, 255), window, 10, 300)

        draw_text('CONTROLES P2', font, (255, 255, 255), window, 450, 175)
        draw_text('WASD', font, (255, 255, 255), window, 450, 260)
        draw_text('BOMBA: ESPAÇO', font, (255, 255, 255), window, 450, 300)

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
        draw_text('JOGAR', font, (0, 0, 0), window, 310, 410)
        draw_text('SAIR', font, (0, 0, 0), window, 330, 510)

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