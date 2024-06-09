from scripts.data import *

# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame


pygame.init()

# ----- Toca e define a músicaS
musica = pygame.mixer.Sound('./assets/matue.mp3')
musica.set_volume(0.1)
musica.play(-1)

explosao = pygame.mixer.Sound("./assets/explosao.mp3")
explosao.set_volume(0.2)

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bomber Smash')

# ----- Configura a fonte
font = pygame.font.SysFont(None, 48)
title = pygame.font.SysFont(None,80)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# ----- Carrega e muda o tamanho das imagens
boneco_img = pygame.image.load('assets/hulk verde.png').convert_alpha()
boneco_img = pygame.transform.scale(boneco_img, (BONECO_WIDTH, 45))
boneco1_img = pygame.image.load('assets/hulk.png').convert_alpha()
boneco1_img = pygame.transform.scale(boneco1_img, (BONECO_WIDTH, BONECO_HEIGHT))
brick_img = pygame.image.load('assets/bricks.png').convert_alpha()
brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT)) 
wood_img = pygame.image.load('assets/wood.png').convert_alpha()
wood_img = pygame.transform.scale(wood_img, (WOOD_WIDTH, WOOD_HEIGHT))
bomb_img=pygame.image.load('assets/bomb.png').convert_alpha()
bomb_img = pygame.transform.scale(bomb_img, (BOMB_WIDTH, BOMB_HEIGHT))
bonecobig_img = pygame.image.load('assets/hulk verde.png').convert_alpha()
bonecobig_img = pygame.transform.scale(bonecobig_img, (300, 300))
boneco1big_img = pygame.image.load('assets/hulk.png').convert_alpha()
boneco1big_img = pygame.transform.scale(boneco1big_img, (300, 300))
sand_img = pygame.image.load('assets/sand.png').convert_alpha()
sand_img = pygame.transform.scale(sand_img, (750, 650))
bg_img = pygame.image.load('assets/bg.jpeg').convert_alpha()
bg_img = pygame.transform.scale(bg_img, (750, 650))
exp1_img=pygame.image.load('assets/exp1.png').convert_alpha()
exp1_img = pygame.transform.scale(exp1_img, (EXP_WIDTH, EXP_HEIGHT))
exp2_img=pygame.image.load('assets/exp2.png').convert_alpha()
exp2_img = pygame.transform.scale(exp2_img, (EXP_WIDTH, EXP_HEIGHT))
exp3_img=pygame.image.load('assets/exp3.png').convert_alpha()
exp3_img = pygame.transform.scale(exp3_img, (EXP_WIDTH, EXP_HEIGHT))
imagem=[bomb_img,exp1_img,exp2_img,exp3_img]

# ----- Configura a tela inicial
click = False