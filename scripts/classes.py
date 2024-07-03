import pygame
from scripts.data import *
from scripts.init import *
from scripts.auxFuncs import *


# Definindo os novos tipos
class TileElement(pygame.sprite.Sprite):
    def __init__(self, img, x, y, width_key, height_key):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * IMAGENS[width_key]["WIDTH"]
        self.rect.y = y * IMAGENS[height_key]["HEIGHT"]
        self.x = x
        self.y = y

class Brick(TileElement):
    def __init__(self, img, x, y):
        super().__init__(img, x, y, "WOOD", "WOOD")


class Wood(TileElement):
    def __init__(self, img, x, y):
        super().__init__(img, x, y, "BRICK", "BRICK")


class Player(pygame.sprite.Sprite):
    def __init__(self, img, all_sprites, all_bombs, x, y):
        # Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x * IMAGENS["BRICK"]["WIDTH"]
        self.rect.y = y * IMAGENS["BRICK"]["HEIGHT"]
        self.all_sprites = all_sprites
        self.all_bombs = all_bombs
        self.x = x
        self.y = y
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 10
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 3000

    def update(self):
        self.rect.x = self.x * IMAGENS["BRICK"]["WIDTH"]
        self.rect.y = self.y * IMAGENS["BRICK"]["HEIGHT"]

    def shoot(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_shot
        if elapsed_ticks > self.shoot_ticks:
            self.last_shot = now
            new_bomb = Bomb(self.rect.bottom + 17, self.rect.centerx + 2, self.x, self.y)
            self.all_sprites.add(new_bomb)
            self.all_bombs.add(new_bomb)


class Player1(Player):
    def win(self):
        win(2)

class Player2(Player):
    def win(self):
        win(1)


class Bomb(pygame.sprite.Sprite):
    # Construtor da classe
    def __init__(self, bottom, centerx,i,j):
        # Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = IMAGENS["BOMB"]["pygameImage"]
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.tempo = 150
        self.expc=centerx
        self.expb=bottom

        self.i = j
        self.j = i

    # Configura a animação da explosão da bomba
    def update(self):
        self.tempo -= 2 

        if self.tempo>30 and self.tempo<=40:
            self.image = IMAGENS["EXPLOSION1"]["pygameImage"]
            centerx=self.expc
            bottom=self.expb
            self.rect.centerx = centerx
            self.rect.bottom = bottom

        if self.tempo == 30:
            SONS["EXPLOSAO"]["pygameSound"].play()

        if self.tempo<=30 and self.tempo>20:
            self.image = IMAGENS["EXPLOSION2"]["pygameImage"]
            centerx=self.expc
            bottom=self.expb
            self.rect.centerx = centerx
            self.rect.bottom = bottom
            
        if self.tempo<=20 and self.tempo>10:
            self.image = IMAGENS["EXPLOSION3"]["pygameImage"]
            centerx=self.expc
            bottom=self.expb
            self.rect.centerx = centerx
            self.rect.bottom = bottom 
    
        if self.tempo <= 5:
            
            centerx =self.expc
            bottom = self.expb
            self.rect.width *= 1 
            self.rect.height *= 1 
            self.rect.centerx = centerx
            self.rect.bottom = bottom

            # Explodindo as caixas 
            hits = pygame.sprite.groupcollide(all_bombs,all_woods,False,False)
            for _, woods in hits.items():
                possiveis = [(self.i + 1, self.j), (self.i - 1, self.j), (self.i, self.j+ 1), (self.i, self.j - 1)]
                for wood in woods:
                    if (wood.y, wood.x) in possiveis:
            
                        MAPA[wood.y][wood.x] = 0
                        wood.kill()

            # Bomba matando o jogador 
            kill = pygame.sprite.groupcollide(all_bombs,all_players,False,False)
    
            for _,players in kill.items():
                possiveis = [(self.i + 1, self.j), (self.i - 1, self.j), (self.i, self.j+ 1), (self.i, self.j - 1),(self.i,self.j)]

                for player in players: 
                        if (player.y,player.x) in possiveis:
                            MAPA[player.y][player.x] = 0
                            player.win()
                            player.kill()
            
            self.kill()
