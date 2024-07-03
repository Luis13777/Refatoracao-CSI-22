from scripts.data import *
import pygame



def init_game ():
        
    pygame.init()
    DISPLAY["pygameDisplay"] = pygame.display.set_mode((DISPLAY["WIDTH"], DISPLAY["HEIGHT"]))
    pygame.display.set_caption(DISPLAY["TITLE"])

    musica = pygame.mixer.Sound(f'./assets/{SONS["MUSICA"]["CAMINHO"]}')
    musica.set_volume(SONS["MUSICA"]["VOLUME"])
    musica.play(-1)
    SONS["MUSICA"]["pygameSound"] = musica

    explosao = pygame.mixer.Sound(f'./assets/{SONS["EXPLOSAO"]["CAMINHO"]}')
    explosao.set_volume(SONS["EXPLOSAO"]["VOLUME"])
    SONS["EXPLOSAO"]["pygameSound"] = explosao


    # ----- Configura a fonte
    FONTS["NORMAL"]["pygameFont"] = pygame.font.SysFont(None, 48)
    FONTS["BIG"]["pygameFont"] = pygame.font.SysFont(None,80)
  
    for imagem in IMAGENS:
        IMAGENS[imagem]["pygameImage"] = pygame.image.load(f'./assets/{IMAGENS[imagem]["CAMINHO"]}').convert_alpha()
        IMAGENS[imagem]["pygameImage"] = pygame.transform.scale(IMAGENS[imagem]["pygameImage"], (IMAGENS[imagem]["WIDTH"], IMAGENS[imagem]["HEIGHT"]))
    

