import pygame
import random
from scripts.data import *
from scripts.init import *
from scripts.classes import *


def game():

    # Criando os blocos do mapa
    for l in range (len(MAPA)):
        for c in range (len(MAPA[l])):
            index = MAPA[l][c]
            
            if cenario[index] == "brick":
                pedra = brick(IMAGENS["BRICK"]["pygameImage"],c,l)
                all_bricks.add(pedra)
            
            if cenario[index] == "air":
                r = random.randint(2,4)
                if r == 3 or r == 4:
                    madeira =wood(IMAGENS["WOOD"]["pygameImage"],c,l)
                    all_woods.add(madeira)
                    MAPA[l][c] = 1
                else:
                    MAPA[l][c] = 0

            if cenario[index] == "player1":
                MAPA[l][c] = 0 
                player1 = Player1(IMAGENS["BONECO1"]["pygameImage"], all_sprites, all_bombs,c,l)
                
            
            if cenario[index] == "player2":
                MAPA[l][c] = 0
                player2 = Player2(IMAGENS["BONECO2"]["pygameImage"],all_sprites, all_bombs,c,l)
                
    # adicionando aos grupos de sprites
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(all_bricks)
    all_sprites.add(all_woods)
    all_blocks.add(all_bricks)
    all_blocks.add(all_woods)
    all_players.add(player1)
    all_players.add(player2)


    game = True
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
                    if MAPA[player1.y][player1.x - 1] in [0,-1] :
                        player1.x -= 1 
            
                if event.key == pygame.K_RIGHT: 
                    if MAPA[player1.y][player1.x + 1] in [0,-1]:
                        player1.x += 1 
            
                if event.key == pygame.K_UP:
                    if MAPA[player1.y - 1][player1.x] in [0,-1]:
                        player1.y -=1
                
                if event.key == pygame.K_DOWN:
                    if MAPA[player1.y + 1][player1.x] in [0,-1]:
                        player1.y +=1
                    
                if event.key == pygame.K_RSHIFT:
                    player1.shoot()
                
                #AÇÕES PLAYER 2

                if event.key == pygame.K_a:
                    if MAPA[player2.y][player2.x - 1] in[0,-1] :
                        player2.x -= 1 
                
                if event.key == pygame.K_d: 
                    if MAPA[player2.y][player2.x + 1] in[0,-1]:
                        player2.x += 1 
                
                if event.key == pygame.K_w:
                    if MAPA[player2.y - 1][player2.x] in[0,-1]:
                        player2.y -=1
                
                if event.key == pygame.K_s:
                    if MAPA[player2.y + 1][player2.x] in[0,-1]:
                        player2.y +=1
                    
                if event.key == pygame.K_SPACE:
                    player2.shoot()
        
    

        # ----- Atualiza estado do jogo
        # Atualizando a posição das sprites
        all_sprites.update()


        # ----- Gera saídas
        DISPLAY["pygameDisplay"] .fill((0, 255, 100))  # Preenche com a cor verde

        DISPLAY["pygameDisplay"] .blit(IMAGENS["SAND"]["pygameImage"],(0,0))


        # Desenhando sprites
        all_sprites.draw(DISPLAY["pygameDisplay"] )

        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
