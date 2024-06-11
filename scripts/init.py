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



    # ----- Configura a fonte
    FONTS["NORMAL"]["pygameFont"] = pygame.font.SysFont(None, 48)
    FONTS["BIG"]["pygameFont"] = pygame.font.SysFont(None,80)
  
    for imagem in IMAGENS:
        IMAGENS[imagem]["pygameImage"] = pygame.image.load(f'./assets/{IMAGENS[imagem]["CAMINHO"]}').convert_alpha()
        IMAGENS[imagem]["pygameImage"] = pygame.transform.scale(IMAGENS[imagem]["pygameImage"], (IMAGENS[imagem]["WIDTH"], IMAGENS[imagem]["HEIGHT"]))
    


    # # ----- Carrega e muda o tamanho das imagens
    # boneco_img = pygame.image.load('assets/hulk verde.png').convert_alpha()
    # boneco_img = pygame.transform.scale(boneco_img, (BONECO_WIDTH, 45))
    # boneco1_img = pygame.image.load('assets/hulk.png').convert_alpha()
    # boneco1_img = pygame.transform.scale(boneco1_img, (BONECO_WIDTH, BONECO_HEIGHT))
    # brick_img = pygame.image.load('assets/bricks.png').convert_alpha()
    # brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT)) 
    # wood_img = pygame.image.load('assets/wood.png').convert_alpha()
    # wood_img = pygame.transform.scale(wood_img, (WOOD_WIDTH, WOOD_HEIGHT))
    # bomb_img=pygame.image.load('assets/bomb.png').convert_alpha()
    # bomb_img = pygame.transform.scale(bomb_img, (BOMB_WIDTH, BOMB_HEIGHT))
    # bonecobig_img = pygame.image.load('assets/hulk verde.png').convert_alpha()
    # bonecobig_img = pygame.transform.scale(bonecobig_img, (300, 300))
    # boneco1big_img = pygame.image.load('assets/hulk.png').convert_alpha()
    # boneco1big_img = pygame.transform.scale(boneco1big_img, (300, 300))
    # sand_img = pygame.image.load('assets/sand.png').convert_alpha()
    # sand_img = pygame.transform.scale(sand_img, (750, 650))
    # bg_img = pygame.image.load('assets/bg.jpeg').convert_alpha()
    # bg_img = pygame.transform.scale(bg_img, (750, 650))
    # exp1_img=pygame.image.load('assets/exp1.png').convert_alpha()
    # exp1_img = pygame.transform.scale(exp1_img, (EXP_WIDTH, EXP_HEIGHT))
    # exp2_img=pygame.image.load('assets/exp2.png').convert_alpha()
    # exp2_img = pygame.transform.scale(exp2_img, (EXP_WIDTH, EXP_HEIGHT))
    # exp3_img=pygame.image.load('assets/exp3.png').convert_alpha()
    # exp3_img = pygame.transform.scale(exp3_img, (EXP_WIDTH, EXP_HEIGHT))
    # imagem=[bomb_img,exp1_img,exp2_img,exp3_img]



    # # Criando um grupo de blocos 
    # all_woods = pygame.sprite.Group()
    # all_bricks = pygame.sprite.Group()

    # # Criando um grupo de sprites
    # all_sprites = pygame.sprite.Group()
    # all_bombs = pygame.sprite.Group()
    # all_blocks = pygame.sprite.Group()
    # all_players = pygame.sprite.Group()

    # # ----- Gera tela principal
    # window = pygame.display.set_mode((WIDTH, HEIGHT))
    # pygame.display.set_caption('Bomber Smash')
    # # ----- Configura a tela inicial
    # click = False



    # game = True
    # # Variável para o ajuste de velocidade
    # clock = pygame.time.Clock()


    # # Criando os blocos do mapa
    # for l in range (len(LAYOUT)):
    #     for c in range (len(LAYOUT[l])):
    #         item = LAYOUT[l][c]
            
    #         if item == 1:
    #             pedra = brick(brick_img,c,l)
    #             all_bricks.add(pedra)
            
    #         if item == 0:
    #             r= random.randint(2,4)
    #             if r ==3 or r==4:
    #                 madeira =wood(wood_img,c,l)
    #                 all_woods.add(madeira)
    #                 LAYOUT[l][c] =1
    #             else:
    #                 LAYOUT[l][c] =0

    #         if item == 5 :

    #             LAYOUT[l][c] =0 
    #             player1 = Player1(boneco_img, all_sprites, all_bombs,c,l,imagem)
                
            
    #         if item == 6:
    #             LAYOUT[l][c] =0
    #             player2 = Player2(boneco1_img,all_sprites, all_bombs,c,l,imagem)
                
    # # adicionando aos grupos de sprites
    # all_sprites.add(player1)
    # all_sprites.add(player2)
    # all_sprites.add(all_bricks)
    # all_sprites.add(all_woods)
    # all_blocks.add(all_bricks)
    # all_blocks.add(all_woods)
    # all_players.add(player1)
    # all_players.add(player2)