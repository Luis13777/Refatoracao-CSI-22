import pygame
from scripts.data import *
from scripts.init import *
from scripts.loadFiles import *

# ----- Configura as telas finais de vitória de cada jogador
def win_p1(window):
    while True:

        window.fill((0, 255, 100))
        window.blit(bg_img, (0,0))

        draw_text('O JOGADOR 1 VENCEU!', title, (255, 255, 255), window, 50, 100)
        window.blit(bonecobig_img, (200, 300))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(250, 200, 230, 40)


        if button_1.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        draw_text('SAIR', font, (0, 0, 0), window, 330, 205)

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

def win_p2(window):
    while True:

        window.fill((0, 255, 100))
        window.blit(bg_img, (0,0))

        draw_text('O JOGADOR 2 VENCEU!', title, (255, 255, 255), window, 50, 100)
        window.blit(boneco1big_img, (200, 300))

        mx, my = pygame.mouse.get_pos()


        button_1 = pygame.Rect(250, 200, 230, 40)

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        draw_text('SAIR', font, (0, 0, 0), window, 330, 205)

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