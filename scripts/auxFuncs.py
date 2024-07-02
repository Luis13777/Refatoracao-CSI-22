import pygame
from scripts.data import *
from scripts.init import *



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# ----- Configura as telas finais de vitória de cada jogador
def win_p1():
    while True:
        window = DISPLAY["pygameDisplay"]
        window.fill((0, 255, 100))
        window.blit(IMAGENS["BACKGROUND"]["pygameImage"], (0,0))

        draw_text('O JOGADOR 1 VENCEU!', FONTS["NORMAL"]["pygameFont"], (255, 255, 255), window, 50, 100)
        window.blit(IMAGENS["BONECO1BIG"]["pygameImage"], (200, 300))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(250, 200, 230, 40)


        if button_1.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        draw_text('SAIR', FONTS["NORMAL"]["pygameFont"], (0, 0, 0), window, 330, 205)

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

def win_p2():
    while True:
        window = DISPLAY["pygameDisplay"]

        window.fill((0, 255, 100))
        window.blit(IMAGENS["BACKGROUND"]["pygameImage"], (0,0))

        draw_text('O JOGADOR 2 VENCEU!', FONTS["NORMAL"]["pygameFont"], (255, 255, 255), window, 50, 100)
        window.blit(IMAGENS["BONECO2BIG"]["pygameImage"], (200, 300))

        mx, my = pygame.mouse.get_pos()


        button_1 = pygame.Rect(250, 200, 230, 40)

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        draw_text('SAIR', FONTS["NORMAL"]["pygameFont"], (0, 0, 0), window, 330, 205)

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