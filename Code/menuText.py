#Imports
import pygame as pg
import os

#Parent sprite class
class SpriteDisplay(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((64,64))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        #No methods needed.

#Child classes. All have the same position
class aimOfGame(SpriteDisplay, pg.sprite.Sprite):#Makes the aim of the game image sprite
    def __init__(self, menu_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(menu_folder, "aimOfGame.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 64)

class tileDisplay(SpriteDisplay, pg.sprite.Sprite):#Makes the tile display image sprite
    def __init__(self, menu_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(menu_folder, "tileDisplay.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 64)

class tileExplain(SpriteDisplay, pg.sprite.Sprite):#Makes the tile explain image sprite
    def __init__(self, menu_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(menu_folder, "tileExplain.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 64)

class itemExplain(SpriteDisplay, pg.sprite.Sprite):#Makes the item explain image sprite
    def __init__(self, menu_folder, screen):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(menu_folder, "itemExplain.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 64)
