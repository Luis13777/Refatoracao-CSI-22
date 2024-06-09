import pygame
from scripts.data import *
from scripts.init import *
import random
from scripts.classes import *


def game():

   


    game = True
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 30



    # Criando os blocos do mapa
    for l in range (len(LAYOUT)):
        for c in range (len(LAYOUT[l])):
            item = LAYOUT[l][c]
            
            if item == 1:
                pedra = brick(brick_img,c,l)
                all_bricks.add(pedra)
            
            if item == 0:
                r= random.randint(2,4)
                if r ==3 or r==4:
                    madeira =wood(wood_img,c,l)
                    all_woods.add(madeira)
                    LAYOUT[l][c] =1
                else:
                    LAYOUT[l][c] =0

            if item == 5 :

                LAYOUT[l][c] =0 
                player1 = Player1(boneco_img, all_sprites, all_bombs,c,l,imagem)
                
            
            if item == 6:
                LAYOUT[l][c] =0
                player2 = Player2(boneco1_img,all_sprites, all_bombs,c,l,imagem)
                
    # adicionando aos grupos de sprites
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(all_bricks)
    all_sprites.add(all_woods)
    all_blocks.add(all_bricks)
    all_blocks.add(all_woods)
    all_players.add(player1)
    all_players.add(player2)



    # ===== Loop principal =====
    while game:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:    
                # AÇÕES PLAYER 1
            
                if event.key == pygame.K_LEFT:
                    if LAYOUT[player1.y][player1.x - 1] in[0,-1] :
                        player1.x -= 1 
            
                if event.key == pygame.K_RIGHT: 
                    if LAYOUT[player1.y][player1.x + 1] in[0,-1]:
                        player1.x += 1 
            
                if event.key == pygame.K_UP:
                    if LAYOUT[player1.y - 1][player1.x] in[0,-1]:
                        player1.y -=1
                
                if event.key == pygame.K_DOWN:
                    if LAYOUT[player1.y + 1][player1.x] in[0,-1]:
                        player1.y +=1
                    
                if event.key == pygame.K_RSHIFT:
                    player1.shoot()
                
                #AÇÕES PLAYER 2

                if event.key == pygame.K_a:
                    if LAYOUT[player2.y][player2.x - 1] in[0,-1] :
                        player2.x -= 1 
                
                if event.key == pygame.K_d: 
                    if LAYOUT[player2.y][player2.x + 1] in[0,-1]:
                        player2.x += 1 
                
                if event.key == pygame.K_w:
                    if LAYOUT[player2.y - 1][player2.x] in[0,-1]:
                        player2.y -=1
                
                if event.key == pygame.K_s:
                    if LAYOUT[player2.y + 1][player2.x] in[0,-1]:
                        player2.y +=1
                    
                if event.key == pygame.K_SPACE:
                    player2.shoot()
        
    

        # ----- Atualiza estado do jogo
        # Atualizando a posição das sprites
        all_sprites.update()


        # ----- Gera saídas
        window.fill((0, 255, 100))  # Preenche com a cor verde

        window.blit(sand_img,(0,0))


        # Desenhando sprites
        all_sprites.draw(window)

        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
