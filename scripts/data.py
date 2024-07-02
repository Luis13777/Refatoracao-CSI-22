import pygame


DISPLAY = {"WIDTH": 750, "HEIGHT": 650, "FPS": 30, "pygameDisplay": None, "TITLE": "Bomber Smash"}

MAPA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1],
    [1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,6,1,],
    [1, -1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,-1,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0,0,1],
    [1, -1 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,-1,1],
    [1, 5, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,-1,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1],
        ]

IMAGENS = {
    "BONECO1": {"CAMINHO": "hulk verde.png", "pygameImage": None, "WIDTH": 45, "HEIGHT": 40},
    "BONECO2": {"CAMINHO": "hulk.png", "pygameImage": None, "WIDTH": 45, "HEIGHT": 40},
    "BONECO1BIG": {"CAMINHO": "hulk verde.png", "pygameImage": None, "WIDTH": 300, "HEIGHT": 300},
    "BONECO2BIG": {"CAMINHO": "hulk.png", "pygameImage": None, "WIDTH": 300, "HEIGHT": 300},
    "BRICK": {"CAMINHO": "bricks.png", "pygameImage": None, "WIDTH": 50, "HEIGHT": 50},
    "WOOD": {"CAMINHO": "wood.png", "pygameImage": None, "WIDTH": 50, "HEIGHT": 50},
    "BOMB": {"CAMINHO": "bomb.png", "pygameImage": None, "WIDTH": 90, "HEIGHT": 90},
    "SAND": {"CAMINHO": "sand.png", "pygameImage": None, "WIDTH": 750, "HEIGHT": 650},
    "EXPLOSION1": {"CAMINHO": "exp1.png", "pygameImage": None, "WIDTH": 100, "HEIGHT": 100},
    "EXPLOSION2": {"CAMINHO": "exp2.png", "pygameImage": None, "WIDTH": 100, "HEIGHT": 100},
    "EXPLOSION3": {"CAMINHO": "exp3.png", "pygameImage": None, "WIDTH": 100, "HEIGHT": 100},
    "BACKGROUND": {"CAMINHO": "bg.jpeg", "pygameImage": None, "WIDTH": 750, "HEIGHT": 650}
}

SONS = {
    "MUSICA": {"CAMINHO": "matue.mp3", "VOLUME": 0.1, "pygameSound": None},
    "EXPLOSAO": {"CAMINHO": "explosao.mp3", "VOLUME": 0.2, "pygameSound": None}
}

FONTS = {
    "NORMAL": {"SIZE": 48, "pygameFont": None}, "BIG": {"SIZE": 80, "pygameFont": None}}

all_woods = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_bombs = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()
all_players = pygame.sprite.Group()

clock = pygame.time.Clock()
FPS = 30